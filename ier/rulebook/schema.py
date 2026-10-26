"""
TODO(you): this is a placeholder shape — rewrite it once you actually have
the rulebook file, matching whatever structure it's provided in (likely
YAML or a spreadsheet of rules). A Rule probably needs at minimum: an id,
which claim category/check type it governs, what evidence it requires,
and any thresholds/parameters a check function needs (e.g. a warranty
throughput limit, a contract availability threshold).
"""

from dataclasses import dataclass, field


@dataclass
class Rule:
    id: str
    description: str
    check_type: str
    requires_evidence: bool = True
    parameters: dict = field(default_factory=dict)
