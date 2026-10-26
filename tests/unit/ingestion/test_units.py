"""
Example of the pattern to follow for every new function: write the test
alongside (or just before) the implementation, with a couple of concrete
cases including at least one edge case.

TODO(you): fill these in as you implement ier.ingestion.units, then add
more test files the same way — one test file per source file, mirroring
the ier/ package layout under tests/unit/.
"""

from ier.ingestion.units import convert, normalize_unit, parse_quantity


def test_parse_quantity_handles_whitespace_and_unit_variants():
    assert parse_quantity("4.2 MWh") == (4.2, "MWh")


def test_normalize_unit_treats_percent_spellings_as_equal():
    assert normalize_unit("%") == normalize_unit("percent")


def test_convert_rejects_incompatible_units():
    # e.g. kW (power) -> kWh (energy) should NOT silently succeed
    pass
