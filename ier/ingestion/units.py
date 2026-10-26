"""
Unit parsing/normalization: kW vs kWh, %, hours, cycles, $/kWh, and the
noise that comes with free-text extraction ("250 kW", "250kW ", "250 KW").

TODO(you): a function to detect a unit from raw text, a function to
normalize unit spelling/case, and a function to convert between
compatible units (e.g. kWh -> MWh) where checks need a common basis. Keep
power (kW) and energy (kWh) clearly distinct — conflating them is a
classic planted-issue category for this kind of tool.

This is a good first module to implement: no external dependencies, pure
functions, easy to unit test case by case (see
tests/unit/ingestion/test_units.py).
"""

from typing import Optional


def parse_quantity(raw_text: str) -> tuple[Optional[float], Optional[str]]:
    """Pull a (number, unit) pair out of free text, e.g. '4.2 MWh' -> (4.2, 'MWh')."""
    raise NotImplementedError


def normalize_unit(unit: str) -> str:
    """Canonicalize a unit string so '%', 'pct', 'percent' etc. compare equal."""
    raise NotImplementedError


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Convert between compatible units; raise if the units aren't compatible."""
    raise NotImplementedError
