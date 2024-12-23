#!/usr/bin/env python3
"""Create a template solution file, and add input files and solutions to solutions.json."""
import argparse
from datetime import date
import itertools
import os
from pathlib import Path
import shutil

def get_next_day(year):
    days = sorted([int(f.stem[4:6]) for f in Path("sols").glob('*') if f.name.startswith(f"{year}") and f.suffix == ".py"])
    for i in itertools.count(1):
        if i not in days:
            return i

def get_multiline(prompt):
    print(prompt)
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)

    return "\n".join(contents)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--day",  type=int, help="Advent of code day.")
    parser.add_argument("-y", "--year", type=int, help="Which year to run.")

    args = parser.parse_args()

    if args.year:
        year = args.year
    else:
        this_year = date.today().year
        year_input = input(f"year (default={this_year}): ")
        year = int(year_input) if year_input else this_year

    if args.day:
        day = args.day
    else:
        next_day = get_next_day(year)
        day_input = input(f"day (default={next_day}): ")
        day = int(day_input) if day_input else next_day

    print(f"year: {year}, day: {day}")
    puzzle_name = f"{year}{day:02}"
    filename = f"sols/{puzzle_name}.py"
    print(filename)
    assert not os.path.exists(filename)
    template_filename = "sols/template.py"
    shutil.copy(template_filename, filename)

if __name__ == "__main__":
    main()
