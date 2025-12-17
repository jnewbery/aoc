#!/usr/bin/env python3
import sys
from functools import cache
import argparse
from datetime import datetime
import enum
import json
from pathlib import Path
from subprocess import run
import tomllib
from lib.display import add_display_arguments, print_grid_results, print_table_results
from lib.results import (
    DisplayFormat,
    Implementation,
    Order,
    PARTS,
    Result,
    RESULTS_DIR,
    DayExecution,
    PartExecution,
)
from lib.utils import iter_year_days

class EXIT_CODES(enum.Enum):
    # Must match utils.EXIT_CODES
    SUCCESS = 0
    NOT_IMPLEMENTED = 38
    NO_INPUT = 39

def get_solution(year: int, day: int, part: int, test: bool) -> str:
    file_path = Path(__file__).resolve().parent.joinpath(f"solutions/{'test' if test else 'full'}/{year}.txt")
    with open(file_path, "r") as f:
        line_num = (day - 1) * 2 + (part - 1)
        return f.readlines()[line_num].strip()

def execute_solver_iterations(day_execution: DayExecution, part_number: int, part_execution: PartExecution) -> None:
    """Run a part solver multiple times, updating part_execution in place."""
    timings: list[int] = []
    for _ in range(part_execution.iterations):
        script_output = run(part_execution.command, capture_output=True, text=True)

        if script_output.returncode == EXIT_CODES.NOT_IMPLEMENTED.value:
            part_execution.result = Result.NOT_IMPLEMENTED
            break
        elif script_output.returncode == EXIT_CODES.NO_INPUT.value:
            part_execution.result = Result.NO_INPUT
            break

        try:
            solver_output = json.loads(script_output.stdout.strip())
        except json.decoder.JSONDecodeError:
            part_execution.result = Result.BAD_OUTPUT
            break
        part_execution.solution = solver_output.get("solution")

        # Validate once, on the first successful iteration.
        if part_execution.result in {Result.UNEXECUTED, Result.SUCCESS}:
            try:
                actual_sol = get_solution(day_execution.year, day_execution.day, part_number, day_execution.test)
                part_execution.expected_solution = actual_sol
            except KeyError:
                part_execution.result = Result.INCONCLUSIVE
                break

            if part_execution.solution != actual_sol:
                part_execution.result = Result.FAILURE
                break
            part_execution.result = Result.SUCCESS

        try:
            timings.append(int(solver_output["execution_time"]))
        except (KeyError, ValueError, TypeError):
            part_execution.result = Result.BAD_OUTPUT
            break

    if part_execution.result == Result.SUCCESS and timings:
        part_execution.execution_time_micro_seconds = int(sum(timings) / len(timings))

def run_solver(day_execution: DayExecution) -> None:
    for part_number, part_execution in day_execution.parts.items():
        part_execution.iterations = day_execution.iterations
        if day_execution.implementation == Implementation.NONE:
            part_execution.result = Result.NOT_IMPLEMENTED
            continue

        execute_solver_iterations(day_execution, part_number, part_execution)

        day_execution.parts[part_number] = part_execution

@cache
def get_manifest() -> dict[tuple[int, int], Implementation]:
    manifest: dict[tuple[int, int], Implementation] = {}
    manifest_path = Path(__file__).resolve().parent.joinpath(".config/manifest.toml")
    with open(manifest_path, "rb") as f:
        t = tomllib.load(f)
    for year, day in iter_year_days():
        if t.get(str(year), {}).get(str(day), None) is not None:
            manifest[(year, day)] = Implementation(t[str(year)][str(day)])
        else:
            manifest[(year, day)] = Implementation.NONE
    return manifest

def get_implementation(implementation: Implementation, year: int, day: int) -> Implementation:
    if implementation != Implementation.MANIFEST:
        return implementation
    return get_manifest().get((year, day), Implementation.NONE)

def get_result_filename(day_execution: DayExecution, part: int) -> Path:
    suffix = "t" if day_execution.test else ""
    return RESULTS_DIR / f"{day_execution.year}{day_execution.day:02}{part}{suffix}.json"

def build_part_result(day_execution: DayExecution, part: int, run_at: str) -> dict | None:
    part_execution = day_execution.parts.get(part)
    if part_execution is None:
        return None
    return {
        "run_at": run_at,
        "year": day_execution.year,
        "day": day_execution.day,
        "part": part,
        "test": day_execution.test,
        "language": day_execution.implementation.display_name,
        "implementation": day_execution.implementation.value,
        "result": part_execution.result.value,
        "solution": part_execution.solution,
        "expected_solution": part_execution.expected_solution,
        "execution_time_micro_seconds": part_execution.execution_time_micro_seconds,
        "command": part_execution.command,
        "iterations": part_execution.iterations,
    }

def save_results(executions: list[DayExecution]) -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    run_at = datetime.now().isoformat()
    for execution in executions:
        for part in execution.parts:
            part_result = build_part_result(execution, part, run_at)
            if part_result is None:
                continue
            with open(get_result_filename(execution, part), "w") as f:
                json.dump(part_result, f, indent=2)

def run_solvers(implementation: Implementation, year_days: list[str], parts: list[int], test: bool, iterations: int) -> list[DayExecution]:
    results: list[DayExecution] = []

    for year_day in year_days:
        year = int(year_day[:4])
        day = int(year_day[4:6])
        parts_dict = {}
        day_implementation = get_implementation(implementation, year, day)
        if day_implementation == Implementation.NONE:
            parts_dict = {part_number: PartExecution(result=Result.NOT_IMPLEMENTED, iterations=iterations) for part_number in parts}
        elif day_implementation == Implementation.MANIFEST:
            raise AssertionError("Implementation should not be MANIFEST at this point")
        else:
            assert day_implementation in {Implementation.PYTHON, Implementation.RUST, Implementation.OCAML}
            commands = [[f"{Path(__file__).parent}/solvers/{day_implementation.value}/run.sh", f"{year_day}{part}", "-v"] for part in parts]
            if test:
                for command in commands:
                    command.append("-t")
            parts_dict = {part_number: PartExecution(command, iterations=iterations) for part_number, command in zip(parts, commands)}
        execution = DayExecution(implementation=day_implementation, year=year, day=day, parts=parts_dict, test=test, iterations=iterations)
        run_solver(execution)
        results.append(execution)

    return results

def main():
    parser = argparse.ArgumentParser()
    add_display_arguments(parser)
    parser.add_argument(
        "--iterations",
        type=int,
        default=3,
        help="Number of times to run each solver; execution time is averaged.",
    )
    parser.add_argument(
        "-i",
        "--implementation",
        type=Implementation,
        choices=[implementation.value for implementation in Implementation],
        default=Implementation.MANIFEST,
        help="Which implementation to run. Pass '@' to use the manifest file."
    )
    parser.add_argument("--build", action=argparse.BooleanOptionalAction, help="Build the solutions before running them", default=True)

    args = parser.parse_args()

    all_days: list[str] = []
    for year, day in iter_year_days():
        all_days.append(f"{year}{day:02}")
    days = [str(day) for day in all_days if str(day).startswith(args.puzzles[:6])]
    if not days:
        print("No days found")
        sys.exit(1)
    parts = [int(args.puzzles[6])] if len(args.puzzles) == 7 else PARTS

    if args.build:
        print("Building solutions...")
        run(["just", "build"])
    results = run_solvers(args.implementation, days, parts, args.test, args.iterations)
    save_results(results)

    if args.format == DisplayFormat.GRID:
        print_grid_results(results)
    else:
        print_table_results(results, args.order)

if __name__ == "__main__":
    main()
