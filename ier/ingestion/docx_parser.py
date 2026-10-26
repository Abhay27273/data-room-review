"""
Word document parsing (O&M plan, some contracts/letters).

TODO(you): implement DocxParser(DocumentParser) using python-docx. Page
numbers don't really exist in a .docx — decide what you'll cite instead
(paragraph index, section heading, or render-to-PDF first and cite pages
from that) and be consistent with whatever the report format expects.
"""

from ier.ingestion.base import DocumentParser


class DocxParser(DocumentParser):
    def can_parse(self, path):
        raise NotImplementedError

    def parse(self, path):
        raise NotImplementedError
