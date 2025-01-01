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

class Order(enum.StrEnum):
    CHRONOLOGICAL = enum.auto()
    EXECUTION_TIME = enum.auto()

@dataclass
class Part:
    result: Result = Result.UNEXECUTED
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

@dataclass
class ExecutionResult:
    year: int
    day: int
    parts: dict[int, Part]
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
        return f"[italic green]{execution_time_micro_seconds}µs"
    elif execution_time_micro_seconds < 100_000:
        return f"[italic green]{execution_time_micro_seconds / 1000:.1f}ms"
    elif execution_time_micro_seconds < 1_000_000:
        return f"[italic green]{int(execution_time_micro_seconds // 1_000)}ms"
    else:
        return f"[italic green]{execution_time_micro_seconds / 1_000_000:.1f}s"

def get_solution(year: int, day: int, part: int, test: bool) -> str:
    file_path = Path(__file__).resolve().parent.joinpath(f"solutions/{'test' if test else 'full'}/{year}.txt")
    with open(file_path, "r") as f:
        line_num = (day - 1) * 2 + (part - 1)
        return f.readlines()[line_num].strip()

def run_solver(result: ExecutionResult) -> None:
    for part_number, part_result in result.parts.items():
        command = [f"{Path(__file__).parent}/solvers/rs/target/release/aoc", "-y", str(result.year), "-d", str(result.day), "-p", str(part_number), "-v"]
        if result.test:
            command.append("-t")

        script_output = run(command, capture_output=True, text=True)

        if script_output.returncode == EXIT_CODES.NOT_IMPLEMENTED.value:
            part_result.result = Result.NOT_IMPLEMENTED
            continue

        try:
            solver_output = json.loads(script_output.stdout.strip())
        except json.decoder.JSONDecodeError:
            part_result.result = Result.BAD_OUTPUT
            continue
        part_result.solution = solver_output["solution"]

        try:
            actual_sol = get_solution(result.year, result.day, part_number, result.test)
        except KeyError:
            part_result.result = Result.INCONCLUSIVE
            continue

        if part_result.solution != actual_sol:
            part_result.result = Result.FAILURE
        else:
            part_result.result = Result.SUCCESS
            part_result.execution_time_micro_seconds = int(solver_output["execution_time"])

        result.parts[part_number] = part_result


def run_solvers(years: list[int], days: list[int], parts: list[int], test: bool) -> list[ExecutionResult]:
    results: list[ExecutionResult] = []

    for year, day in product(years, days):
        parts_dict = {part: Part() for part in parts}
        result = ExecutionResult(year=year, day=day, parts=parts_dict, test=test)
        run_solver(result)
        if result.implemented:
            results.append(result)

    return results

def print_year_results(year: int, results: list[ExecutionResult], order: Order, console: Console) -> None:
    if order == Order.CHRONOLOGICAL:
        results.sort(key=lambda result: result.day)
    else:
        assert order == Order.EXECUTION_TIME
        results.sort(key=lambda result: result.total_execution_time or 0, reverse=True)
    part1s = [result.parts[1] for result in results if result.parts.get(1, None) is not None]
    part2s = [result.parts[2] for result in results if result.parts.get(2, None) is not None]
    table = Table(title=f"{year} Results" , row_styles=["", "on grey23"])
    table.add_column("Day", style="bold")
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
        if part1s:
            row.append(part1.result_str if part1 else f"[bold blue]Unexecuted")
            row.append(format_execution_time(part1.execution_time_micro_seconds) if part1 else "")
        if part2s:
            row.append(part2.result_str if part2 else f"[bold blue]Unexecuted")
            row.append(format_execution_time(part2.execution_time_micro_seconds) if part2 else "")
        row.append(format_execution_time(result.total_execution_time))
        table.add_row(*row)

    if table.row_count > 1:
        # Add a total row
        table.add_section()
        total_row = ["TOTAL"]
        if part1s:
            total_row.append(f"[bold green]COMPLETE" if all(result.result == Result.SUCCESS for result in part1s) else f"[bold blue]INCOMPLETE")
            total_row.append(format_execution_time(sum([result.execution_time_micro_seconds for result in part1s if result.execution_time_micro_seconds is not None])))
        if part2s:
            total_row.append(f"[bold green]COMPLETE" if all(result.result == Result.SUCCESS for result in part2s) else f"[bold blue]INCOMPLETE")
            total_row.append(format_execution_time(sum([result.execution_time_micro_seconds for result in part2s if result.execution_time_micro_seconds is not None])))
        total_row.append(format_execution_time(sum([result.total_execution_time for result in results if result.total_execution_time is not None])))
        table.add_row(*total_row)

    if table.row_count > 0:
        console.print(table)

def print_results(results: list[ExecutionResult], order: Order) -> None:
    console = Console()
    for year in sorted({result.year for result in results}):
        print_year_results(year, [result for result in results if result.year == year], order, console)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", "--args",  action="store_true", help="Print args")
    parser.add_argument("-y", "--year", default=None, help=f"Which year to run. Default is to run all years")
    parser.add_argument("-d", "--day",  type=int, help="Advent of code day. Leave blank to run all days.")
    parser.add_argument("-p", "--part", type=int, help="Which part to run. Leave blank to run both parts.")
    parser.add_argument("-t", "--test", action="store_true", help="Whether to run with test input. If false, runs with full input.")
    parser.add_argument("-o", "--order", type=Order, choices=[order.value for order in Order], default=Order.CHRONOLOGICAL, help="Order to display results in.")

    args = parser.parse_args()


    years = [int(args.year)] if args.year else list(range(2015, date.today().year + 1))
    days = [args.day] if args.day else list(range(1, 26))
    parts = [args.part] if args.part else [1, 2]

    if args.args:
        print(f"years: {years}")
        print(f"days: {days}")
        print(f"test: {args.test}")
        print(f"parts: {parts}")

    print("Building solutions...")
    run(["just", "build"])
    results = run_solvers(years, days, parts, args.test)

    print_results(results, args.order)

if __name__ == "__main__":
    main()
