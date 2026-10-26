"""
Text-layer PDF parsing (company overview, spec sheets, certificates,
contracts that were produced digitally rather than scanned).

TODO(you): implement PdfParser(DocumentParser) using pdfplumber or
pymupdf. Walk pages, pull text (and tables where present), and tag every
fact with its page number. Detect pages that have no extractable text
layer (likely scanned) and hand those off to ocr_parser instead of
returning empty results for them.
"""

from ier.ingestion.base import DocumentParser


class PdfParser(DocumentParser):
    def can_parse(self, path):
        raise NotImplementedError

    def parse(self, path):
        raise NotImplementedError
