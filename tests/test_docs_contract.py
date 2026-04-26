from pathlib import Path

from tests.docs_inventory import DEEP_DOCS, ROOT_DOCS

REQUIRED_META_KEYS = ("audience", "last_updated", "related_docs")
REQUIRED_SECTION_NAMES = ("Purpose", "Current State", "Verification Notes", "Related Docs")

TRACE_DOCS = [
    Path("README.md"),
    Path("ARCHITECTURE.md"),
    Path("OPERATIONS.md"),
    Path("docs/developer/codebase-and-workflows.md"),
    Path("docs/operations/runtime-and-maintenance.md"),
]


def _parse_leading_metadata(content: str) -> dict[str, str]:
    metadata: dict[str, str] = {}
    for line in content.splitlines():
        stripped = line.strip()
        if not stripped:
            break
        if ":" not in stripped:
            break
        key, value = stripped.split(":", 1)
        metadata[key.strip()] = value.strip()
    return metadata


def _collect_h2_sections(content: str) -> set[str]:
    sections: set[str] = set()
    for line in content.splitlines():
        if line.startswith("## "):
            sections.add(line.removeprefix("## ").strip())
    return sections


def test_deep_docs_follow_contract() -> None:
    for path in DEEP_DOCS:
        assert path.exists(), f"missing {path}"
        content = path.read_text(encoding="utf-8")
        metadata = _parse_leading_metadata(content)
        assert metadata.get("audience"), f"{path} must start with non-empty audience metadata"
        missing_metadata = [key for key in REQUIRED_META_KEYS if not metadata.get(key)]
        assert not missing_metadata, f"{path} missing metadata keys {missing_metadata}"

        sections = _collect_h2_sections(content)
        missing_sections = [name for name in REQUIRED_SECTION_NAMES if name not in sections]
        assert not missing_sections, f"{path} missing H2 sections {missing_sections}"


def test_traceability_and_recommendation_labels_present() -> None:
    for path in TRACE_DOCS:
        content = path.read_text(encoding="utf-8")
        sections = _collect_h2_sections(content)
        assert "Current State" in sections, f"{path} missing Current State section"
        assert "Verification Notes" in sections, f"{path} missing Verification Notes section"
    backlog = Path("docs/improvements/documentation-backlog.md").read_text(encoding="utf-8")
    entries = [line.strip() for line in backlog.splitlines() if line.strip().startswith("- title:")]
    assert len(entries) >= 2, "backlog must contain at least two recommendation entries"
    for field in ("status:", "rationale:", "expected_impact:", "date_opened:"):
        assert backlog.count(field) >= len(entries), f"backlog missing per-entry field {field}"


def test_contributor_and_operator_docs_include_core_workflows() -> None:
    contrib = Path("CONTRIBUTING.md").read_text(encoding="utf-8")
    assert "pytest -v" in contrib
    assert "docs/README.md" in contrib
    assert "uv run --extra dev pytest -q" in contrib

    ops = Path("docs/operations/runtime-and-maintenance.md").read_text(encoding="utf-8")
    for cmd in [
        "python -m exec_operating_system.cli ingest",
        "python -m exec_operating_system.cli query",
        "python -m exec_operating_system.cli lint",
    ]:
        assert cmd in ops


def test_docs_baseline_sections_present_in_root_docs() -> None:
    for path in ROOT_DOCS:
        content = path.read_text(encoding="utf-8")
        sections = _collect_h2_sections(content)
        for required in REQUIRED_SECTION_NAMES:
            assert required in sections, f"{path} missing section {required}"
