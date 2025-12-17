from itertools import groupby
from operator import attrgetter
from rich import box
from rich.columns import Columns
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from .results_lib import (
    Order,
    Result,
    PARTS,
    aggregate_total_time,
    format_execution_time,
)


def _year_groups(results):
    # Helper to group sorted results by year.
    for year, year_results in groupby(sorted(results, key=attrgetter("year", "day")), key=attrgetter("year")):
        yield year, list(year_results)


def print_year_results(year: int, results, order: Order, console: Console) -> None:
    if order == Order.CHRONOLOGICAL:
        results.sort(key=lambda result: result.day)
    else:
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


def print_table_results(results, order: Order) -> None:
    console = Console()
    for year, year_results in _year_groups(results):
        print_year_results(year, year_results, order, console)

    total_time = sum([result.total_execution_time for result in results if result.total_execution_time is not None])
    total_stars = len([1 for day_result in results for part_result in day_result.parts.values() if part_result.result == Result.SUCCESS])
    console.print(f"Total stars: {total_stars} ⭐️, Total time: {format_execution_time(total_time)}", highlight=False)


def get_day_cell(day_result) -> Text:
    if day_result is None:
        return Text("x", style="grey30 on grey8")

    part_results = [day_result.parts.get(part_num) for part_num in PARTS]
    successes = sum(1 for part in part_results if part and part.result == Result.SUCCESS)
    failures = any(part and part.result == Result.FAILURE for part in part_results)
    not_implemented = part_results and all(part and part.result == Result.NOT_IMPLEMENTED for part in part_results if part)

    if successes == len([part for part in part_results if part]) and successes > 0:
        return Text("★", style="gold1")
    if successes > 0:
        return Text("★", style="grey53")
    if failures:
        return Text("x", style="bold red")
    if not_implemented or not any(part_results):
        return Text("·", style="grey53")
    return Text("x", style="bold red")


def build_year_panel(year: int, results) -> Panel:
    # Ensure day order is stable regardless of how results were loaded.
    ordered_results = sorted(results, key=attrgetter("day"))
    day_lookup = {day_result.day: day_result for day_result in ordered_results}
    cells = [get_day_cell(d) for d in day_lookup.values()]

    if len(results) == 25:
        width = 5
    elif len(results) == 12:
        width = 4
    else:
        assert False, "Unsupported number of days for grid display"
    grid = Table.grid(padding=(0, 1))
    for start in range(0, len(cells), width):
        grid.add_row(*cells[start:start + width])

    year_time = aggregate_total_time(results)
    total_time_str = format_execution_time(year_time) if year_time is not None else "[TBD]"
    year_stars = sum(1 for day_result in results for part_result in day_result.parts.values() if part_result.result == Result.SUCCESS)

    stars_txt = Text(f"Stars: {year_stars}/{len(results) * 2}", style="grey85")
    time_txt = Text(f"Time: {total_time_str}", style="grey85")
    content = Group(grid, "", stars_txt, time_txt)

    return Panel(
        content,
        title=f"{year}",
        padding=(1, 2),
        border_style="grey85",
        box=box.ROUNDED,
    )


def print_grid_results(results) -> None:
    console = Console()
    panels = []
    for year, year_results in _year_groups(results):
        if not year_results:
            continue
        panels.append(build_year_panel(year, year_results))

    if panels:
        console.print(Columns(panels, equal=True, expand=True, padding=(1, 2)))

    overall_time = aggregate_total_time(results)
    overall_time_str = format_execution_time(overall_time) if overall_time is not None else "[TBD]"
    total_stars = len([1 for day_result in results for part_result in day_result.parts.values() if part_result.result == Result.SUCCESS])
    console.print(f"Total stars: {total_stars} ⭐️, Total time: {overall_time_str}", highlight=False)
