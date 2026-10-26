"""
Scanned-page handling. Kept as a separate interface from PdfParser so the
OCR engine itself is swappable (pytesseract now, something else later)
without touching the PDF-walking logic.

TODO(you): implement OcrEngine.read_page using pytesseract (render the
page to an image with pymupdf/pdf2image first). Record a confidence score
per fact — OCR noise is explicitly in scope to handle, not ignore — and
keep the page image/bbox so a human reviewer can double check a
low-confidence read against the source.
"""

from abc import ABC, abstractmethod

from ier.ingestion.base import DocumentParser


class OcrEngine(ABC):
    """Reads text out of a page image. Swappable: pytesseract today, a
    cloud OCR API or local vision model later, same interface."""

    @abstractmethod
    def read_page(self, image) -> list[tuple[str, float]]:
        """Return (text_fragment, confidence) pairs found on the page image."""
        raise NotImplementedError


class ScannedPdfParser(DocumentParser):
    """Uses an OcrEngine to parse pages a text-layer parser couldn't read."""

    def __init__(self, ocr_engine: OcrEngine):
        self.ocr_engine = ocr_engine

    def can_parse(self, path):
        raise NotImplementedError

    def parse(self, path):
        raise NotImplementedError
