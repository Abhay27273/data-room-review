"""
The one data shape every parser must produce, so everything downstream
(evidence register, checks) can cite a source without caring which parser
produced the fact. This is the most foundational file in the project —
build and test it first.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class SourceLocation:
    """Where in a document a fact came from — this is what a citation
    points to.

    TODO(you): decide the exact shape per file type. A PDF needs a page
    number; a spreadsheet needs a sheet name + cell reference; a scanned
    page might also want a bounding box if you want to highlight the
    region OCR read from. Keep it precise enough that "every citation
    points to a page or cell that actually supports it" (acceptance
    criterion) holds.
    """

    file_path: str
    page: Optional[int] = None
    sheet: Optional[str] = None
    cell: Optional[str] = None
    bbox: Optional[tuple] = None


@dataclass(frozen=True)
class ExtractedFact:
    """One atomic fact pulled out of a document, with its unit and
    provenance.

    TODO(you): add whatever fields the evidence/checks stages need — e.g.
    raw_text (what the parser actually read, before interpretation), a
    normalized numeric value + unit (see units.py), and a confidence
    score for OCR'd text so low-confidence reads can be flagged rather
    than silently trusted.
    """

    value: object
    unit: Optional[str]
    source: SourceLocation
    raw_text: str
    confidence: float = 1.0
