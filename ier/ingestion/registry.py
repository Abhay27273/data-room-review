"""
Dispatches a file path to the right DocumentParser by extension (and, for
PDFs, by whether the page has a text layer or needs OCR).

TODO(you): a ParserRegistry that holds a list of DocumentParser instances
and returns the first one whose can_parse(path) is True. This should be
the only place that knows about file extensions — add a new format by
registering a new parser, not by branching deeper in the pipeline.
"""

from pathlib import Path

from ier.ingestion.base import DocumentParser
from ier.ingestion.schema import ExtractedFact


class ParserRegistry:
    def __init__(self, parsers: list[DocumentParser]):
        self.parsers = parsers

    def parse_file(self, path: Path) -> list[ExtractedFact]:
        raise NotImplementedError

    def parse_data_room(self, root: Path) -> list[ExtractedFact]:
        """Walk every file under a data-room folder and parse it."""
        raise NotImplementedError
