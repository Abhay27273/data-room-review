# <project name>

TODO(you): one or two sentences on what this does, matching the brief's
objective (data room -> evidence register, checks, independent-engineer
style report).

## Setup

TODO(you): fill in as the real steps stabilize. Roughly:

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env    # then fill in your API key(s)
```

Requires Python 3.10+ (the code uses `list[...]`/`X | None` type hints).

Tesseract OCR must be installed separately and on PATH for scanned-page
parsing (see `ier/ingestion/ocr_parser.py`) — not a pip package.

## Running it

```
python -m ier.cli ingest --data-room data/provided/data_rooms/room_1 --out outputs/room_1
```

Runs ingestion (PDF + spreadsheet parsing) over a data room and writes
`facts.json` (every extracted fact with its source) and `unparsed.json`
(files no parser could handle) to the output folder. Everything past
ingestion (evidence extraction, checks, report, `evaluate` command) is
still TODO.

## Project layout

See DESIGN_NOTE.md for the architecture rationale. One flat module per
pipeline stage under `ier/` rather than a subpackage per stage — the
earlier scaffold's many single-class files were overkill for a POC:

- `units.py` — unit parsing/conversion (kW/kWh, %, hours, cycles, $/kWh)
- `ingestion.py` — parsers (PDF, scanned/OCR, spreadsheet, docx) -> `ExtractedFact`, `ParserRegistry`
- `models.py` — swappable LLM provider interface + schema-validated calls
- `evidence.py` — the evidence register (`Claim`, `EvidenceStatus`)
- `rulebook.py` — loads the rulebook we're given
- `checks.py` — rulebook-driven checks -> pass / fail / can't check
- `impact_claims.py` — carbon/life-cycle claim checks
- `standards.py` — fetches + caches external published standards
- `readiness.py` — business-risk classification + lender-criterion scoring
- `report.py` — assembles everything into the provided report format
- `evaluation.py` — scores tool output against the labeled test rooms
- `config.py`, `cli.py` — settings and the command-line entry point

`tests/unit/` mirrors this flat layout. `data/provided/` holds materials
given to us (see its own README); `cache/` and `outputs/` are git-ignored
run artifacts.

## Known gaps

TODO(you): per the deliverable list — what's not done or known to be weak.
