from ier.units import convert, normalize_unit, parse_quantity


def test_parse_quantity_handles_whitespace_and_unit_variants():
    assert parse_quantity("4.2 MWh") == (4.2, "MWh")


def test_normalize_unit_treats_percent_spellings_as_equal():
    assert normalize_unit("%") == normalize_unit("percent")


def test_convert_rejects_incompatible_units():
    pass
