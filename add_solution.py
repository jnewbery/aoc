#!/usr/bin/env python3
"""Add solutions to solutions.json."""
from datetime import date
import json

def main():
    this_year = date.today().year
    year_input = input(f"year (default={this_year}): ")
    year = int(year_input) if year_input else this_year

    day_input = input("day: ")
    day = int(day_input)

    part_input = input("part: ")
    part = str(int(part_input))

    solution_type_input = input("Test solution? (y/n): ")
    solution_type = "test" if solution_type_input == "y" else "full"

    solution = input("Enter solution: ")

    print(f"year: {year}, day: {day}, part: {part}, type: {solution_type}, solution: {solution}")
    puzzle_name = f"{year}{day:02}"

    with open("sols/solutions.json", "r") as f:
        solutions = json.load(f)

    if puzzle_name not in solutions:
        solutions[puzzle_name] = {}

    if part not in solutions[puzzle_name]:
        solutions[puzzle_name][part] = {}

    if solutions[puzzle_name][part].get(solution_type):
        if input("Solution already exists! Overwrite? (y/n): ") != "y":
            return

    solutions[puzzle_name][part][solution_type] = solution

    with open("sols/solutions.json", "w") as f:
        json.dump(solutions, f, indent=2)

if __name__ == "__main__":
    main()
