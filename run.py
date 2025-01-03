#!/usr/bin/env python3
import sys
from functools import cache
import argparse
from datetime import date
import enum
import json
from pathlib import Path
from subprocess import run
from itertools import product
from rich.console import Console
from rich.table import Table
from dataclasses import dataclass, field
import tomllib

YEARS = list(range(2015, date.today().year + 1))
DAYS = list(range(1, 26))
PARTS = [1, 2]

class EXIT_CODES(enum.Enum):
    # Must match utils.EXIT_CODES
    SUCCESS = 0
    NOT_IMPLEMENTED = 38

class Result(enum.StrEnum):
    UNEXECUTED = enum.auto()
    SUCCESS = enum.auto()
    FAILURE = enum.auto()
    INCONCLUSIVE = enum.auto()
    NOT_IMPLEMENTED = enum.auto()
    BAD_OUTPUT = enum.auto()

class Order(enum.StrEnum):
    CHRONOLOGICAL = enum.auto()
    EXECUTION_TIME = enum.auto()

class Implementation(enum.StrEnum):
    OCAML = "ml"
    PYTHON = "py"
    RUST = "rs"
    MANIFEST = "@"
    NONE = enum.auto()

    @property
    def display_name(self) -> str:
        match self:
            case Implementation.OCAML:
                return "OCaml"
            case Implementation.PYTHON:
                return "Python"
            case Implementation.RUST:
                return "Rust"
            case _:
                return self.value

@dataclass
class PartExecution:
    command: list[str] = field(default_factory=list)
    result: Result = Result.UNEXECUTED
    solution: str | None = None
    execution_time_micro_seconds: int | None = None

    @property
    def result_str(self) -> str:
        if self.result == Result.SUCCESS:
            return f"⭐ [green]{self.solution}[/green]"
        elif self.result == Result.FAILURE:
            return f"[red]{self.solution}[/red]"
        elif self.result == Result.INCONCLUSIVE:
            return f"[yellow]Inconclusive[/yellow]"
        elif self.result == Result.NOT_IMPLEMENTED:
            return f"[blue]Not Implemented[/blue]"
        elif self.result == Result.BAD_OUTPUT:
            return f"[red]Bad Output[/red]"
        else:
            return f"[blue]Unexecuted[/blue]"

@dataclass
class DayExecution:
    implementation: Implementation
    year: int
    day: int
    parts: dict[int, PartExecution]
    test: bool

    @property
    def total_execution_time(self) -> int | None:
        return sum(part.execution_time_micro_seconds for part in self.parts.values() if part.execution_time_micro_seconds is not None)

    @property
    def implemented(self) -> bool:
        return all(part.result != Result.NOT_IMPLEMENTED for part in self.parts.values())

def format_execution_time(execution_time_micro_seconds: int| None) -> str:
    if execution_time_micro_seconds is None:
        return ""
    if execution_time_micro_seconds < 1000:
        return f"{execution_time_micro_seconds}µs"
    elif execution_time_micro_seconds < 100_000:
        return f"{execution_time_micro_seconds / 1000:.1f}ms"
    elif execution_time_micro_seconds < 1_000_000:
        return f"{int(execution_time_micro_seconds // 1_000)}ms"
    else:
        return f"{execution_time_micro_seconds / 1_000_000:.1f}s"

def get_solution(year: int, day: int, part: int, test: bool) -> str:
    file_path = Path(__file__).resolve().parent.joinpath(f"solutions/{'test' if test else 'full'}/{year}.txt")
    with open(file_path, "r") as f:
        line_num = (day - 1) * 2 + (part - 1)
        return f.readlines()[line_num].strip()

def run_solver(day_execution: DayExecution) -> None:
    for part_number, part_execution in day_execution.parts.items():
        if day_execution.implementation == Implementation.NONE:
            part_execution.result = Result.NOT_IMPLEMENTED
            continue

        script_output = run(part_execution.command, capture_output=True, text=True)

        if script_output.returncode == EXIT_CODES.NOT_IMPLEMENTED.value:
            part_execution.result = Result.NOT_IMPLEMENTED
            continue

        try:
            solver_output = json.loads(script_output.stdout.strip())
        except json.decoder.JSONDecodeError:
            part_execution.result = Result.BAD_OUTPUT
            continue
        part_execution.solution = solver_output["solution"]

        try:
            actual_sol = get_solution(day_execution.year, day_execution.day, part_number, day_execution.test)
        except KeyError:
            part_execution.result = Result.INCONCLUSIVE
            continue

        if part_execution.solution != actual_sol:
            part_execution.result = Result.FAILURE
        else:
            part_execution.result = Result.SUCCESS
            part_execution.execution_time_micro_seconds = int(solver_output["execution_time"])

        day_execution.parts[part_number] = part_execution

@cache
def get_manifest() -> dict[tuple[int, int], Implementation]:
    manifest: dict[tuple[int, int], Implementation] = {}
    manifest_path = Path(__file__).resolve().parent.joinpath(".config/manifest.toml")
    with open(manifest_path, "rb") as f:
        t = tomllib.load(f)
    for day, year in product(DAYS, YEARS):
        if t.get(str(year), {}).get(str(day), None) is not None:
            manifest[(year, day)] = Implementation(t[str(year)][str(day)])
        else:
            manifest[(year, day)] = Implementation.NONE
    return manifest

def get_implementation(implementation: Implementation, year: int, day: int) -> Implementation:
    if implementation != Implementation.MANIFEST:
        return implementation
    return get_manifest().get((year, day), Implementation.NONE)

def run_solvers(implementation: Implementation, year_days: list[str], parts: list[int], test: bool) -> list[DayExecution]:
    results: list[DayExecution] = []

    for year_day in year_days:
        year = int(year_day[:4])
        day = int(year_day[4:6])
        parts_dict = {}
        day_implementation = get_implementation(implementation, year, day)
        if day_implementation == Implementation.NONE:
            parts_dict = {part_number: PartExecution(result=Result.NOT_IMPLEMENTED) for part_number in parts}
        elif day_implementation == Implementation.PYTHON:
            command = [f"{Path(__file__).parent}/solvers/py/{year}{day:02}.py"]
            if test:
                command.append("-t")
            parts_dict = {part_number: PartExecution(command + [str(part_number), "-v"]) for part_number in parts}
        elif day_implementation == Implementation.RUST:
            commands = [[f"{Path(__file__).parent}/solvers/rs/target/release/aoc", f"{year_day}{part}", "-v"] for part in parts]
            if test:
                for command in commands:
                    command.append("-t")
            parts_dict = {part_number: PartExecution(command) for part_number, command in zip(parts, commands)}
        elif day_implementation == Implementation.OCAML:
            commands = [[f"{Path(__file__).parent}/solvers/ml/_build/default/main.exe", f"{year_day}{part}"] for part in parts]
            if test:
                for command in commands:
                    command.append("-t")
            parts_dict = {part_number: PartExecution(command) for part_number, command in zip(parts, commands)}
        execution = DayExecution(implementation=day_implementation, year=year, day=day, parts=parts_dict, test=test)
        run_solver(execution)
        results.append(execution)

    return results

def print_year_results(year: int, results: list[DayExecution], order: Order, console: Console) -> None:
    if order == Order.CHRONOLOGICAL:
        results.sort(key=lambda result: result.day)
    else:
        assert order == Order.EXECUTION_TIME
        results.sort(key=lambda result: result.total_execution_time or 0, reverse=True)
    part1s = [result.parts[1] for result in results if result.parts.get(1, None) is not None]
    part2s = [result.parts[2] for result in results if result.parts.get(2, None) is not None]
    table = Table(title=f"{year} Results" , row_styles=["", "on grey23"])
    table.add_column("Day", style="bold")
    table.add_column("Implementation", header_style="bold")
    if part1s:
        table.add_column("Part 1")
        table.add_column("(time)", style="italic", header_style="italic")
    if part2s:
        table.add_column("Part 2")
        table.add_column("(time)", style="italic", header_style="italic")
    table.add_column("Total Time", style="italic", header_style="italic")

    for result in results:
        part1 = result.parts.get(1, None)
        part2 = result.parts.get(2, None)
        if (part1 == None or part1.result == Result.NOT_IMPLEMENTED) and (part2 == None or part2.result == Result.NOT_IMPLEMENTED):
            continue
        row = [f"Day {result.day}"]
        row.append(f"{result.implementation.display_name}")
        if part1s:
            row.append(part1.result_str if part1 else f"[bold blue]Unexecuted")
            row.append(f"[italic green]{format_execution_time(part1.execution_time_micro_seconds)}" if part1 else "")
        if part2s:
            row.append(part2.result_str if part2 else f"[bold blue]Unexecuted")
            row.append(f"[italic green]{format_execution_time(part2.execution_time_micro_seconds)}" if part2 else "")
        row.append(f"[italic green]{format_execution_time(result.total_execution_time)}")
        table.add_row(*row)

    if table.row_count > 0:
        # Add a total row
        table.add_section()
        total_row = ["TOTAL", ""]
        if part1s:
            total_row.append(f"[bold green]COMPLETE" if all(result.result == Result.SUCCESS for result in part1s) else f"[bold blue]INCOMPLETE")
            total_row.append(f"[italic green]{format_execution_time(sum([result.execution_time_micro_seconds for result in part1s if result.execution_time_micro_seconds is not None]))}")
        if part2s:
            total_row.append(f"[bold green]COMPLETE" if all(result.result == Result.SUCCESS for result in part2s) else f"[bold blue]INCOMPLETE")
            total_row.append(f"[italic green]{format_execution_time(sum([result.execution_time_micro_seconds for result in part2s if result.execution_time_micro_seconds is not None]))}")
        total_row.append(f"[italic green]{format_execution_time(sum([result.total_execution_time for result in results if result.total_execution_time is not None]))}")
        table.add_row(*total_row)

        console.print(table)

def print_results(results: list[DayExecution], order: Order) -> None:
    console = Console()
    for year in sorted({result.year for result in results}):
        print_year_results(year, [result for result in results if result.year == year], order, console)

    total_time = sum([result.total_execution_time for result in results if result.total_execution_time is not None])
    total_stars = len([1 for day_result in results for part_result in day_result.parts.values() if part_result.result == Result.SUCCESS])
    console.print(f"Total stars: {total_stars} ⭐️, Total time: {format_execution_time(total_time)}", highlight=False)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("puzzles", help=f"Which puzzles to run, in format YYYYDDP. Any prefix can be used. For example, pass 2015 to run all puzzles from 2015, or 201501 to run both parts of day 1 from 2015.")
    parser.add_argument("-t", "--test", action="store_true", help="Whether to run with test input. If false, runs with full input.")
    parser.add_argument(
        "-i",
        "--implementation",
        type=Implementation,
        choices=[implementation.value for implementation in Implementation],
        default=Implementation.MANIFEST,
        help="Which implementation to run. Pass '@' to use the manifest file."
    )
    parser.add_argument("-o", "--order", type=Order, choices=[order.value for order in Order], default=Order.CHRONOLOGICAL, help="Order to display results in.")

    args = parser.parse_args()

    all_days = [f"{year}{day:02}" for year, day in product(YEARS, DAYS)]
    days = [str(day) for day in all_days if str(day).startswith(args.puzzles[:6])]
    if not days:
        print("No days found")
        sys.exit(1)
    parts = [int(args.puzzles[6])] if len(args.puzzles) == 7 else PARTS

    print("Building solutions...")
    run(["just", "build"])
    results = run_solvers(args.implementation, days, parts, args.test)

    print_results(results, args.order)

if __name__ == "__main__":
    main()
