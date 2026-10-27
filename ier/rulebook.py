from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass
class Rule:
    id: str
    description: str
    check_type: str
    requires_evidence: bool = True
    parameters: dict = field(default_factory=dict)


def load_rulebook(path: Path) -> list[Rule]:
    raw_rules = yaml.safe_load(Path(path).read_text())

    rules = []
    for raw in raw_rules:
        rules.append(Rule(
            id=raw["id"],
            description=raw["description"],
            check_type=raw["check_type"],
            requires_evidence=raw.get("requires_evidence", True),
            parameters=raw.get("parameters", {}),
        ))
    return rules
