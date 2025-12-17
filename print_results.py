#!/usr/bin/env python3
import argparse
import json
import sys
from lib.display import print_grid_results, print_table_results
from lib.results import (
    DayExecution,
    DisplayFormat,
    Implementation,
    Order,
    PARTS,
    PartExecution,
    Result,
    RESULTS_DIR,
)


def load_results(puzzles: str, parts: list[int], test: bool) -> list[DayExecution]:
    if not RESULTS_DIR.exists():
        return []

    day_prefix = puzzles[:6]
    results: dict[tuple[int, int, bool], DayExecution] = {}
    for path in RESULTS_DIR.glob("*.json"):
        stem = path.stem
        has_test_suffix = stem.endswith("t")
        if has_test_suffix != test:
            continue
        if len(stem) < 7:
            continue
        try:
            year = int(stem[:4])
            day = int(stem[4:6])
            part = int(stem[6])
        except ValueError:
            continue

        if parts and part not in parts:
            continue
        day_id = f"{year}{day:02}"
        if day_prefix and not day_id.startswith(day_prefix):
            continue

        with open(path) as f:
            data = json.load(f)

        try:
            implementation = Implementation(data.get("implementation"))
        except Exception:
            implementation = Implementation.NONE

        key = (year, day, has_test_suffix)
        if key not in results:
            results[key] = DayExecution(
                implementation=implementation,
                year=year,
                day=day,
                parts={},
                test=bool(data.get("test", has_test_suffix)),
            )
        elif results[key].implementation == Implementation.NONE:
            results[key].implementation = implementation

        try:
            result_enum = Result(data.get("result"))
        except Exception:
            result_enum = Result.UNEXECUTED

        results[key].parts[part] = PartExecution(
            command=data.get("command", []),
            result=result_enum,
            solution=data.get("solution"),
            execution_time_micro_seconds=data.get("execution_time_micro_seconds"),
            expected_solution=data.get("expected_solution"),
        )

    return list(results.values())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("puzzles", nargs="?", default="", help="Which puzzles to print, in format YYYYDDP. Any prefix can be used.")
    parser.add_argument("-t", "--test", action="store_true", help="Whether to read test results. If false, reads full results.")
    parser.add_argument("-o", "--order", type=Order, choices=[order.value for order in Order], default=Order.CHRONOLOGICAL, help="Order to display results in.")
    parser.add_argument("-f", "--format", type=DisplayFormat, choices=[fmt.value for fmt in DisplayFormat], default=DisplayFormat.TABLE, help="Output format to display results in. 'grid' prints a calendar-style view.")
    args = parser.parse_args()

    parts = [int(args.puzzles[6])] if len(args.puzzles) == 7 else PARTS
    results = load_results(args.puzzles, parts, args.test)

    if not results:
        print("No results found")
        sys.exit(1)

    if args.format == DisplayFormat.GRID:
        print_grid_results(results)
    else:
        print_table_results(results, args.order)


if __name__ == "__main__":
    main()
