# Provided materials go here

Drop the files you receive into these subfolders, keeping original
names/structure where reasonable so paths in config/CLI args stay stable:

- `primer/` — the primer + worked example + glossary (how a lender looks
  at a storage project)
- `rulebook/` — the rulebook that drives `ier/rulebook/loader.py`
- `standards_reference_list/` — the list of published standards (infra
  classification, bankability, independent-engineer scope, LCA) — this is
  the *list*, not the standards themselves, which get fetched + cached
  under `./cache` at run time
- `report_format/` — the report format to match in `ier/report/`
- `worked_example/` — the one worked example report
- `data_rooms/` — the four synthetic data rooms + labels
  - `room_1/`, `room_2/`, `room_3/`, `room_4/`
  - `labels/` — claim statuses + planted issues for each room
