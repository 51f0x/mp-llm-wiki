from __future__ import annotations

from typing import Any

import yaml

REQUIRED_STANDARD = {
    "title",
    "domain",
    "last_updated",
    "source_refs",
    "confidence",
    "sensitivity",
    "related_pages",
}

REQUIRED_DECISION = {
    "decision_id",
    "status",
    "context",
    "options_considered",
    "rationale",
    "impact_areas",
}


def parse_frontmatter(content: str) -> tuple[dict[str, Any], str]:
    if not content.startswith("---"):
        return {}, content
    lines = content.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return {}, content
    end = 1
    while end < len(lines) and lines[end].rstrip() != "---":
        end += 1
    if end >= len(lines):
        return {}, content
    yaml_str = "".join(lines[1:end])
    body = "".join(lines[end + 1 :])
    try:
        loaded = yaml.safe_load(yaml_str)
    except yaml.YAMLError:
        return {}, content
    if not isinstance(loaded, dict):
        return {}, content
    return loaded, body


def validate_frontmatter(meta: dict[str, Any], is_decision: bool) -> list[str]:
    required = REQUIRED_DECISION if is_decision else REQUIRED_STANDARD
    missing = [k for k in required if k not in meta]
    return sorted(missing)
