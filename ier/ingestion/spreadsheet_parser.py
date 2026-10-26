from pathlib import Path

import openpyxl

from ier.ingestion.base import DocumentParser
from ier.ingestion.schema import ExtractedFact, SourceLocation
from ier.ingestion.units import parse_quantity


class SpreadsheetParser(DocumentParser):
    def can_parse(self, path: Path) -> bool:
        return path.suffix.lower() in (".xlsx", ".xlsm")

    def parse(self, path: Path) -> list[ExtractedFact]:
        workbook = openpyxl.load_workbook(path, data_only=True)
        facts = []

        for sheet in workbook.worksheets:
            for row in sheet.iter_rows():
                for cell in row:
                    if cell.value is None:
                        continue
                    facts.append(self._fact_from_cell(path, sheet.title, cell))

        return facts

    def _fact_from_cell(self, path: Path, sheet_name: str, cell) -> ExtractedFact:
        raw_text = str(cell.value)
        source = SourceLocation(file_path=str(path), sheet=sheet_name, cell=cell.coordinate)

        if isinstance(cell.value, (int, float)):
            return ExtractedFact(value=cell.value, unit=None, source=source, raw_text=raw_text)

        value, unit = parse_quantity(raw_text)
        if value is not None:
            return ExtractedFact(value=value, unit=unit, source=source, raw_text=raw_text)

        return ExtractedFact(value=cell.value, unit=None, source=source, raw_text=raw_text)
