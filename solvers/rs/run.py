#!/usr/bin/env python3
import argparse
from datetime import date
import enum
import json
from pathlib import Path
from subprocess import run
from itertools import product
from rich.console import Console
from rich.table import Table
from dataclasses import dataclass

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

@dataclass
class ExecutionResult:
    year: int
    day: int
    part: int
    test: bool
    result: str = Result.UNEXECUTED
    solution: str | None = None
    execution_time_micro_seconds: int | None = None

    @property
    def result_str(self) -> str:
        if self.result == Result.SUCCESS:
            return f"[green]{self.solution}"
        elif self.result == Result.FAILURE:
            return f"[red]{self.solution}"
        elif self.result == Result.INCONCLUSIVE:
            return f"[yellow]Inconclusive"
        elif self.result == Result.NOT_IMPLEMENTED:
            return f"[blue]Not Implemented"
        elif self.result == Result.BAD_OUTPUT:
            return f"[red]Bad Output"
        else:
            return f"[blue]Unexecuted"

def format_execution_time(execution_time_micro_seconds: int| None) -> str:
    if execution_time_micro_seconds is None:
        return ""
    if execution_time_micro_seconds < 1000:
        return f"[italic green]{execution_time_micro_seconds}µs"
    elif execution_time_micro_seconds < 100_000:
        return f"[italic green]{execution_time_micro_seconds / 1000:.1f}ms"
    elif execution_time_micro_seconds < 1_000_000:
        return f"[italic green]{int(execution_time_micro_seconds // 1_000)}ms"
    else:
        return f"[italic green]{execution_time_micro_seconds / 1_000_000:.1f}s"

def get_solution(year: int, day: int, part: int, test: bool) -> str:
    # print(f"Reading solution for {day} part {part} {'test' if test else 'full'}")
    file_path = Path(f"../../solutions/{'test' if test else 'full'}/{year}.txt")
    with open(file_path, "r") as f:
        line_num = (day - 1) * 2 + (part - 1)
        return f.readlines()[line_num].strip()

def run_solver(result: ExecutionResult) -> None:
    command = ["./target/release/aoc", "-y", str(result.year), "-d", str(result.day), "-p", str(result.part), "-v"]
    if result.test:
        command.append("-t")

    script_output = run(command, capture_output=True, text=True)

    if script_output.returncode == EXIT_CODES.NOT_IMPLEMENTED.value:
        result.result = Result.NOT_IMPLEMENTED
        return

    try:
        solver_output = json.loads(script_output.stdout.strip())
    except json.decoder.JSONDecodeError:
        result.result = Result.BAD_OUTPUT
        return
    result.solution = solver_output["solution"]
    result.execution_time_micro_seconds = int(solver_output["execution_time"])

    try:
        actual_sol = get_solution(result.year, result.day, result.part, result.test)
    except KeyError:
        result.result = Result.INCONCLUSIVE
        return

    if result.solution != actual_sol:
        result.result = Result.FAILURE
    else:
        result.result = Result.SUCCESS


def run_solvers(years: list[int], days: list[int], parts: list[int], test: bool) -> list[ExecutionResult]:
    results: list[ExecutionResult] = []

    for year, day, part in product(years, days, parts):
        result = ExecutionResult(year=year, day=day, part=part, test=test)
        run_solver(result)
        results.append(result)

    return results

def print_year_results(year: int, results: list[ExecutionResult], console: Console) -> None:
    table = Table(title=f"{year} Results" , row_styles=["", "on grey23"])
    table.add_column("Day", style="bold")
    table.add_column("Part 1")
    table.add_column("(time)", style="italic", header_style="italic")
    table.add_column("Part 2")
    table.add_column("(time)", style="italic", header_style="italic")

    for day in {result.day for result in results}: 
        part1 = next((result for result in results if result.day == day and result.part == 1), None)
        part2 = next((result for result in results if result.day == day and result.part == 2), None)
        if (part1 == None or part1.result == Result.NOT_IMPLEMENTED) and (part2 == None or part2.result == Result.NOT_IMPLEMENTED):
            continue
        table.add_row(
            f"Day {day}",
            part1.result_str if part1 else f"[bold blue]Unexecuted",
            format_execution_time(part1.execution_time_micro_seconds) if part1 else "",
            part2.result_str if part2 else f"[bold blue]Unexecuted",
            format_execution_time(part2.execution_time_micro_seconds) if part2 else ""
        )

    if table.row_count > 0:
        table.add_section()
        part1_outcome = f"[bold green]COMPLETE" if all(result.result == Result.SUCCESS for result in results if result.part == 1) else f"[bold blue]INCOMPLETE"
        total_part1_times = sum([result.execution_time_micro_seconds for result in results if result.part == 1 and result.execution_time_micro_seconds is not None])
        part2_outcome = f"[bold green]COMPLETE" if all(result.result == Result.SUCCESS for result in results if result.part == 2) else f"[bold blue]INCOMPLETE"
        total_part2_times = sum([result.execution_time_micro_seconds for result in results if result.part == 2 and result.execution_time_micro_seconds is not None])
        table.add_row("TOTAL", part1_outcome, format_execution_time(total_part1_times), part2_outcome, format_execution_time(total_part2_times))
        console.print(table)

def print_results(results: list[ExecutionResult]) -> None:
    console = Console()
    for year in sorted({result.year for result in results}):
        print_year_results(year, [result for result in results if result.year == year], console)

def main():
    this_year = date.today().year

    parser = argparse.ArgumentParser()

    parser.add_argument("-a", "--args",  action="store_true", help="Print args")
    parser.add_argument("-d", "--day",  type=int, help="Advent of code day. Leave blank to run all days.")
    parser.add_argument("-t", "--test", action="store_true", help="Whether to run with test input. If false, runs with full input.")
    parser.add_argument("-p", "--part", type=int, help="Which part to run. Leave blank to run both parts.")
    parser.add_argument("-y", "--year", default=None, help=f"Which year to run. Default is to run all years")

    args = parser.parse_args()

    all_years = list(range(2015, this_year + 1))

    if not args.year:
        years = all_years
    else:
        years = [int(args.year)]

    if not args.day:
        days = list(range(1, 26))
    else:
        days = [args.day]

    if not args.part:
        parts = [1, 2]
    else:
        parts = [args.part]

    if args.args:
        print(f"years: {years}")
        print(f"days: {days}")
        print(f"test: {args.test}")
        print(f"parts: {parts}")

    print("Building solutions...")
    run(["cargo", "build", "--release"])
    results = run_solvers(years, days, parts, args.test)

    print_results(results)

if __name__ == "__main__":
    main()
