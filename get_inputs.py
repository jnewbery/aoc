#!/usr/bin/env python3

import argparse
import requests
from pathlib import Path
import datetime

BASE_URL = "http://adventofcode.com/"

FIRST_YEAR = 2015
DAYS_IN_YEAR = 25
PUZZLES: dict[int, int] = {
    2015: 25,
    2016: 25,
    2017: 25,
    2018: 25,
    2019: 25,
    2020: 25,
    2021: 25,
    2022: 25,
    2023: 25,
    2024: 25,
    2025: 12,
}

def get_input(year: int, day: int, cookie: dict[str, str]) -> str:
    url = f'{BASE_URL}{year}/day/{day}/input'
    resp = requests.get(url, cookies=cookie)
    if resp.status_code != 200:
        raise Exception(f"Failed to get input for {year} day {day}. {resp.status_code}: {resp.text}")

    return resp.text

def _main(in_year: int | None, in_day: int | None, overwrite: bool):
    cookies = {}
    with open(".config/cookie.txt") as f:
        cookie_str = f.read().strip()
        for cookie_pair in cookie_str.split("; "):
            key, value = cookie_pair.split("=")
            cookies[key] = value

    today = datetime.datetime.now()
    years = [in_year] if in_year else list(PUZZLES.keys())
    for year in years:
        days = [in_day] if in_day else list(range(1, PUZZLES[year] + 1))
        for day in days:
            if year == today.year and day > today.day:
                print(f"Skipping input for {year} day {day} - it's in the future")
                continue
            # Be considerate of the server - request inputs serially
            input_file = Path(f"inputs/full/{year}{day:02}.txt")

            if input_file.exists() and not overwrite:
                print(f"Input file for {year} day {day} already exists")
                continue

            try:
                input_text = get_input(year, day, cookies)
            except Exception as e:
                print(e)
                continue

            first_line = input_text.splitlines()[0]
            if len(first_line) > 30:
                first_line = first_line[:30] + " ..."
            print(f"Writing input file for {year} day {day}: {first_line}")
            with open(input_file, 'w') as f:
                f.write(input_text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--year', '-y', type=int, default=None, help='Year of the advent of code')
    parser.add_argument('--day', '-d', type=int, default=None, help='Day of the advent of code')
    parser.add_argument('--overwrite', '-o', action='store_true', default=False, help='Overwrite the input file if it exists')
    args = parser.parse_args()

    _main(args.year, args.day, args.overwrite)
