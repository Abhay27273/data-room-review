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

TODO(you): fill in the actual CLI commands once `ier/cli.py` works, e.g.:

```
python -m ier.cli run --data-room data/provided/data_rooms/room_1 --out outputs/room_1
python -m ier.cli evaluate
```

## Project layout

See DESIGN_NOTE.md for the architecture rationale. Top level:

- `ier/` — the tool itself:
  - `ingestion/` — parsers (PDF, scanned/OCR, spreadsheet, docx) -> `ExtractedFact`
  - `models/` — swappable LLM provider interface + schema-validated calls
  - `evidence/` — the evidence register (`Claim`, `EvidenceStatus`)
  - `rulebook/` — loads the rulebook we're given
  - `checks/` — rulebook-driven checks -> pass / fail / can't check
  - `impact_claims/` — carbon/life-cycle claim checks
  - `standards/` — fetches + caches external published standards
  - `readiness/` — business-risk classification + lender-criterion scoring
  - `report/` — assembles everything into the provided report format
  - `evaluation/` — scores tool output against the labeled test rooms
- `tests/` — unit tests, mirrors `ier/`
- `data/provided/` — materials given to us (see its own README)
- `cache/` — cached web-fetched standards (git-ignored)
- `outputs/` — generated evidence registers / reports / eval results (git-ignored)

## Known gaps

TODO(you): per the deliverable list — what's not done or known to be weak.
