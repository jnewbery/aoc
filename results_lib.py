import enum
from dataclasses import dataclass, field
from pathlib import Path

# Shared constants
PARTS = [1, 2]
RESULTS_DIR = Path(__file__).resolve().parent.joinpath("results")


class Result(enum.StrEnum):
    UNEXECUTED = enum.auto()
    SUCCESS = enum.auto()
    FAILURE = enum.auto()
    INCONCLUSIVE = enum.auto()
    NOT_IMPLEMENTED = enum.auto()
    NO_INPUT = enum.auto()
    BAD_OUTPUT = enum.auto()


class Order(enum.StrEnum):
    CHRONOLOGICAL = enum.auto()
    EXECUTION_TIME = enum.auto()


class DisplayFormat(enum.StrEnum):
    TABLE = enum.auto()
    GRID = enum.auto()


class Implementation(enum.StrEnum):
    OCAML = "ml"
    PYTHON = "py"
    RUST = "rs"
    MANIFEST = "@"
    NONE = enum.auto()

    @property
    def display_name(self) -> str:
        match self:
            case Implementation.OCAML:
                return "OCaml"
            case Implementation.PYTHON:
                return "Python"
            case Implementation.RUST:
                return "Rust"
            case _:
                return self.value


@dataclass
class PartExecution:
    command: list[str] = field(default_factory=list)
    result: Result = Result.UNEXECUTED
    solution: str | None = None
    execution_time_micro_seconds: int | None = None
    expected_solution: str | None = None

    @property
    def result_str(self) -> str:
        if self.result == Result.SUCCESS:
            return f"⭐ [green]{self.solution}[/green]"
        elif self.result == Result.FAILURE:
            return f"[red]{self.solution}[/red]"
        elif self.result == Result.INCONCLUSIVE:
            return f"[yellow]Inconclusive[/yellow]"
        elif self.result == Result.NOT_IMPLEMENTED:
            return f"[blue]Not Implemented[/blue]"
        elif self.result == Result.NO_INPUT:
            return f"[blue]No Input[/blue]"
        elif self.result == Result.BAD_OUTPUT:
            return f"[red]Bad Output[/red]"
        else:
            return f"[blue]Unexecuted[/blue]"


@dataclass
class DayExecution:
    implementation: Implementation
    year: int
    day: int
    parts: dict[int, PartExecution]
    test: bool

    @property
    def total_execution_time(self) -> int | None:
        return sum(part.execution_time_micro_seconds for part in self.parts.values() if part.execution_time_micro_seconds is not None)

    @property
    def implemented(self) -> bool:
        return all(part.result != Result.NOT_IMPLEMENTED for part in self.parts.values())


def format_execution_time(execution_time_micro_seconds: int | None) -> str:
    if execution_time_micro_seconds is None:
        return ""
    if execution_time_micro_seconds < 1000:
        return f"{execution_time_micro_seconds}µs"
    elif execution_time_micro_seconds < 100_000:
        return f"{execution_time_micro_seconds / 1000:.1f}ms"
    elif execution_time_micro_seconds < 1_000_000:
        return f"{int(execution_time_micro_seconds // 1_000)}ms"
    else:
        return f"{execution_time_micro_seconds / 1_000_000:.1f}s"


def aggregate_total_time(executions: list[DayExecution]) -> int | None:
    times = [result.total_execution_time for result in executions if result.total_execution_time is not None]
    if not times:
        return None
    return sum(times)
