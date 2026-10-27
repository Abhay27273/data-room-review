import json
from dataclasses import asdict
from pathlib import Path

import click

from ier.ingestion import ParserRegistry, PdfParser, SpreadsheetParser


@click.group()
def main():
    pass


@main.command()
@click.option("--data-room", required=True, type=click.Path(exists=True, path_type=Path))
@click.option("--out", required=True, type=click.Path(path_type=Path))
def ingest(data_room: Path, out: Path):
    registry = ParserRegistry([PdfParser(), SpreadsheetParser()])
    facts, unparsed = registry.parse_data_room(data_room)

    out.mkdir(parents=True, exist_ok=True)
    (out / "facts.json").write_text(json.dumps([asdict(f) for f in facts], indent=2, default=str))
    (out / "unparsed.json").write_text(json.dumps([str(p) for p in unparsed], indent=2))

    click.echo(f"extracted {len(facts)} facts, {len(unparsed)} files unparsed")


if __name__ == "__main__":
    main()
