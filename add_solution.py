#!/usr/bin/env python3

import argparse
import requests
from pathlib import Path
import datetime

BASE_URL = "http://adventofcode.com/"

FIRST_YEAR = 2015
THIS_YEAR = datetime.date.today().year
DAYS_IN_YEAR = 25

def get_input(year: int, day: int, cookie: dict[str, str]) -> str:
    url = f'{BASE_URL}{year}/day/{day}/input'
    resp = requests.get(url, cookies=cookie)
    if resp.status_code != 200:
        raise Exception(f"Failed to get input for {year} day {day}. {resp.status_code}: {resp.text}")

    return resp.text

def _main(year: int | None, day: int | None, test: bool):
    if year is None:
        year_input = input("Enter the year of the advent of code: ")
        if not year_input.isdigit():
            raise ValueError("Invalid year")
        year = int(year_input)
    if year < FIRST_YEAR or year > THIS_YEAR:
        raise ValueError(f"Year must be between {FIRST_YEAR} and {THIS_YEAR}")

    if day is None:
        day_input = input("Enter the day of the advent of code: ")
        if not day_input.isdigit():
            raise ValueError("Invalid day")
        day = int(day_input)
    if day < 1 or day > DAYS_IN_YEAR:
        raise ValueError(f"Day must be between 1 and {DAYS_IN_YEAR}")

    solutions_file = Path(__file__).parent / "solutions" / f"{'test' if test else 'full'}/{year}.txt"
    new_solutions_file = solutions_file.parent / f"{year}.txt.new"

    with open(solutions_file) as f:
        lines = f.readlines()
        if len(lines) < day * 2:
            lines.extend(["\n"] * (day * 2 - len(lines)))

        old_part1 = lines[day * 2 - 2].strip()
        old_part1_prompt = f"Current part 1 solution: {old_part1}" if old_part1 else "No current part 1 solution"
        new_part1 = input(f"{old_part1_prompt}. Enter new part 1 solution (leave blank to keep the same): ")
        if new_part1 != "":
            lines[day * 2 - 2] = new_part1 + "\n"

        old_part2 = lines[day * 2 - 1].strip()
        old_part2_prompt = f"Current part 2 solution: {old_part2}" if old_part2 else "No current part 2 solution"
        new_part2 = input(f"{old_part2_prompt}. Enter new part 2 solution (leave blank to keep the same): ")
        if new_part2 != "":
            lines[day * 2 - 1] = new_part2 + "\n"

        with open(new_solutions_file, 'w') as f:
            f.writelines(lines)

    # Move the new file to the old file
    new_solutions_file.rename(solutions_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--year', '-y', type=int, default=None, help='Year of the advent of code')
    parser.add_argument('--day', '-d', type=int, default=None, help='Day of the advent of code')
    parser.add_argument('--test', '-t', action='store_true', default=False, help='Whether to add the test solution. Defaults to False')
    args = parser.parse_args()

    _main(args.year, args.day, args.test)
