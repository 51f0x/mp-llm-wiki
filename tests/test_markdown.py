from exec_operating_system.markdown import parse_frontmatter, validate_frontmatter


def test_validate_standard_wiki_frontmatter():
    doc = """---
title: Q2 Hiring Plan
domain: people
last_updated: 2026-04-26
source_refs: ["raw/2026-04-26-hiring-notes.md"]
confidence: medium
sensitivity: normal
related_pages: ["wiki/strategy/workforce-plan.md"]
---
body
"""
    meta, _ = parse_frontmatter(doc)
    assert validate_frontmatter(meta, is_decision=False) == []


def test_validate_decision_frontmatter_requires_standard_union():
    meta = {
        "decision_id": "DEC-001",
        "status": "approved",
        "context": "Need a hiring plan decision",
        "options_considered": ["freeze", "hire selectively"],
        "rationale": "Selective hiring keeps momentum",
        "impact_areas": ["people", "execution"],
    }
    assert validate_frontmatter(meta, is_decision=True) == [
        "confidence",
        "domain",
        "last_updated",
        "related_pages",
        "sensitivity",
        "source_refs",
        "title",
    ]
