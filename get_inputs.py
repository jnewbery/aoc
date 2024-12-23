#!/usr/bin/env python3

import argparse
import requests
from pathlib import Path
import datetime
from itertools import product

BASE_URL = "http://adventofcode.com/"

FIRST_YEAR = 2015
DAYS_IN_YEAR = 25

def get_input(year: int, day: int, cookie: dict[str, str]) -> str:
    url = f'{BASE_URL}{year}/day/{day}/input'
    resp = requests.get(url, cookies=cookie)
    if resp.status_code != 200:
        raise Exception(f"Failed to get input for {year} day {day}. {resp.status_code}: {resp.text}")

    return resp.text

def _main(year: int | None, day: int | None, overwrite: bool):
    cookies = {}
    with open(".config/cookie.txt") as f:
        cookie_str = f.read().strip()
        for cookie_pair in cookie_str.split("; "):
            key, value = cookie_pair.split("=")
            cookies[key] = value

    today = datetime.date.today()
    years = [year] if year else list(range(FIRST_YEAR, today.year + 1))
    days = [day] if day else list(range(1, DAYS_IN_YEAR + 1))
    for year, day in product(years, days):
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
