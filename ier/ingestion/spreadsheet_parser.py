"""
Multi-sheet spreadsheet parsing (operating data, financial model, warranty
tables). Cell-level provenance matters here more than anywhere else, since
a lot of the numeric checks (uptime, degradation, contract thresholds)
trace back to a specific cell.

TODO(you): implement SpreadsheetParser(DocumentParser) using openpyxl.
Walk every sheet and every populated cell; for cells that are formulas,
decide whether you record the formula, the computed value, or both (you'll
want the computed value for checks, but the formula is useful evidence for
the "arithmetic inside a document" check).
"""

from ier.ingestion.base import DocumentParser


class SpreadsheetParser(DocumentParser):
    def can_parse(self, path):
        raise NotImplementedError

    def parse(self, path):
        raise NotImplementedError
