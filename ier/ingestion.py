from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import openpyxl
import pdfplumber

from ier.units import parse_quantity


@dataclass(frozen=True)
class SourceLocation:
    file_path: str
    page: Optional[int] = None
    sheet: Optional[str] = None
    cell: Optional[str] = None
    bbox: Optional[tuple] = None


@dataclass(frozen=True)
class ExtractedFact:
    value: object
    unit: Optional[str]
    source: SourceLocation
    raw_text: str
    confidence: float = 1.0


class DocumentParser(ABC):
    @abstractmethod
    def can_parse(self, path: Path) -> bool:
        raise NotImplementedError

    @abstractmethod
    def parse(self, path: Path) -> list[ExtractedFact]:
        raise NotImplementedError


class PdfParser(DocumentParser):
    def can_parse(self, path: Path) -> bool:
        return path.suffix.lower() == ".pdf"

    def parse(self, path: Path) -> list[ExtractedFact]:
        facts = []

        with pdfplumber.open(path) as pdf:
            for page_number, page in enumerate(pdf.pages, start=1):
                text = page.extract_text()
                source = SourceLocation(file_path=str(path), page=page_number)

                if not text or not text.strip():
                    facts.append(ExtractedFact(value=None, unit=None, source=source,
                                                raw_text="no text layer - needs OCR", confidence=0.0))
                    continue

                for line in text.splitlines():
                    line = line.strip()
                    if not line:
                        continue
                    value, unit = parse_quantity(line)
                    facts.append(ExtractedFact(value=value, unit=unit, source=source, raw_text=line))

        return facts


class OcrEngine(ABC):
    @abstractmethod
    def read_page(self, image) -> list[tuple[str, float]]:
        raise NotImplementedError


class ScannedPdfParser(DocumentParser):
    def __init__(self, ocr_engine: OcrEngine):
        self.ocr_engine = ocr_engine

    def can_parse(self, path: Path) -> bool:
        raise NotImplementedError

    def parse(self, path: Path) -> list[ExtractedFact]:
        raise NotImplementedError


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


class DocxParser(DocumentParser):
    def can_parse(self, path: Path) -> bool:
        raise NotImplementedError

    def parse(self, path: Path) -> list[ExtractedFact]:
        raise NotImplementedError


class ParserRegistry:
    def __init__(self, parsers: list[DocumentParser]):
        self.parsers = parsers

    def parse_file(self, path: Path) -> list[ExtractedFact]:
        for parser in self.parsers:
            if parser.can_parse(path):
                return parser.parse(path)
        raise ValueError(f"no parser registered for {path}")

    def parse_data_room(self, root: Path) -> tuple[list[ExtractedFact], list[Path]]:
        facts = []
        unparsed = []

        for path in root.rglob("*"):
            if not path.is_file():
                continue
            try:
                facts.extend(self.parse_file(path))
            except ValueError:
                unparsed.append(path)

        return facts, unparsed
