"""The interface every document parser implements, so the registry can
dispatch by file type without the rest of the tool knowing the difference
between a PDF, a spreadsheet and a scanned page."""

from abc import ABC, abstractmethod
from pathlib import Path

from ier.ingestion.schema import ExtractedFact


class DocumentParser(ABC):
    """Turns one file into a list of provenance-tagged facts.

    TODO(you): implement one subclass per file type (pdf_parser.py,
    spreadsheet_parser.py, docx_parser.py). Each must still produce
    ExtractedFacts even when it can only partially parse a file — a
    parser that silently drops a page breaks the "missing evidence is
    reported, not skipped" requirement further up the pipeline.
    """

    @abstractmethod
    def can_parse(self, path: Path) -> bool:
        """Whether this parser handles the given file (usually by extension)."""
        raise NotImplementedError

    @abstractmethod
    def parse(self, path: Path) -> list[ExtractedFact]:
        """Extract every fact this parser can find, each with its source location."""
        raise NotImplementedError
