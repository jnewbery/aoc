from typing import Generator

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


def iter_year_days() -> Generator[tuple[int, int], None, None]:
    """Return an ordered iterator of (year, day) combinations."""
    for year, no_puzzles in PUZZLES.items():
        for day in range(1, no_puzzles + 1):
            yield year, day
