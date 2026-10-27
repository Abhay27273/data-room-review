import re
from typing import Optional

_NUMBER = r"[-+]?\d{1,3}(?:,\d{3})*(?:\.\d+)?|[-+]?\d+(?:\.\d+)?"
_UNIT = r"\$?/?[A-Za-z]+(?:[/-][A-Za-z]+)*|%"
_QUANTITY_RE = re.compile(rf"(?P<currency>\$)?\s*(?P<number>{_NUMBER})\s*(?P<unit>{_UNIT})?")

_ALIASES = {
    "kw": "kW", "kilowatt": "kW", "kilowatts": "kW",
    "mw": "MW", "megawatt": "MW", "megawatts": "MW",
    "kwh": "kWh", "kilowatthour": "kWh", "kilowatthours": "kWh",
    "mwh": "MWh", "megawatthour": "MWh", "megawatthours": "MWh",
    "gwh": "GWh",
    "%": "%", "pct": "%", "percent": "%", "percentage": "%",
    "h": "h", "hr": "h", "hrs": "h", "hour": "h", "hours": "h",
    "day": "day", "days": "day",
    "yr": "yr", "yrs": "yr", "year": "yr", "years": "yr",
    "cycle": "cycles", "cycles": "cycles",
    "$": "$", "usd": "$",
    "$/kwh": "$/kWh", "usd/kwh": "$/kWh",
    "$/mwh": "$/MWh", "usd/mwh": "$/MWh",
    "$/kw": "$/kW", "usd/kw": "$/kW",
}

_DIMENSION = {
    "kW": "power", "MW": "power",
    "kWh": "energy", "MWh": "energy", "GWh": "energy",
    "%": "percentage",
    "h": "time", "day": "time", "yr": "time",
    "cycles": "cycles",
    "$": "currency",
    "$/kWh": "price_per_energy", "$/MWh": "price_per_energy",
    "$/kW": "price_per_power",
}

_FACTOR = {
    "kW": 1, "MW": 1_000,
    "kWh": 1, "MWh": 1_000, "GWh": 1_000_000,
    "%": 1,
    "h": 1, "day": 24, "yr": 8_760,
    "cycles": 1,
    "$": 1,
    "$/kWh": 1, "$/MWh": 0.001,
    "$/kW": 1,
}


def parse_quantity(raw_text: str) -> tuple[Optional[float], Optional[str]]:
    if not raw_text:
        return None, None

    match = _QUANTITY_RE.search(raw_text)
    if not match:
        return None, None

    try:
        value = float(match.group("number").replace(",", ""))
    except ValueError:
        return None, None

    unit = match.group("unit")
    if match.group("currency"):
        if unit and unit.startswith("/"):
            unit = f"${unit}"
        elif not unit:
            unit = "$"

    return value, unit


def normalize_unit(unit: str) -> str:
    key = re.sub(r"[\s_-]", "", unit.strip().lower())
    try:
        return _ALIASES[key]
    except KeyError:
        raise ValueError(f"unrecognized unit: {unit!r}") from None


def convert(value: float, from_unit: str, to_unit: str) -> float:
    from_canon = normalize_unit(from_unit)
    to_canon = normalize_unit(to_unit)

    from_dim = _DIMENSION[from_canon]
    to_dim = _DIMENSION[to_canon]
    if from_dim != to_dim:
        raise ValueError(f"can't convert {from_canon} ({from_dim}) to {to_canon} ({to_dim})")

    return value * _FACTOR[from_canon] / _FACTOR[to_canon]
