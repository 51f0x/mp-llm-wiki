from pathlib import Path

DEEP_DOCS = [
    Path("docs/executive/strategy-and-value.md"),
    Path("docs/developer/codebase-and-workflows.md"),
    Path("docs/operations/runtime-and-maintenance.md"),
    Path("docs/reference/glossary-and-contracts.md"),
    Path("docs/improvements/documentation-backlog.md"),
]

REQUIRED_META_KEYS = ["audience:", "last_updated:", "related_docs:"]
REQUIRED_SECTIONS = [
    "## Purpose",
    "## Current State",
    "## Verification Notes",
    "## Related Docs",
]

TRACE_DOCS = [
    Path("README.md"),
    Path("ARCHITECTURE.md"),
    Path("OPERATIONS.md"),
    Path("docs/developer/codebase-and-workflows.md"),
    Path("docs/operations/runtime-and-maintenance.md"),
]


def test_deep_docs_follow_contract() -> None:
    for path in DEEP_DOCS:
        assert path.exists(), f"missing {path}"
        content = path.read_text(encoding="utf-8")
        lines = [line for line in content.splitlines() if line.strip()]
        assert lines[0].startswith("audience:"), f"{path} must start with audience metadata"
        for key in REQUIRED_META_KEYS:
            assert key in content, f"{path} missing metadata key {key}"
        for section in REQUIRED_SECTIONS:
            assert section in content, f"{path} missing section {section}"


def test_traceability_and_recommendation_labels_present() -> None:
    for path in TRACE_DOCS:
        content = path.read_text(encoding="utf-8")
        assert "## Current State" in content, f"{path} missing Current State"
        assert "## Verification Notes" in content, f"{path} missing Verification Notes"
    backlog = Path("docs/improvements/documentation-backlog.md").read_text(encoding="utf-8")
    assert "status:" in backlog
    assert "rationale:" in backlog
    assert "expected_impact:" in backlog
    assert "date_opened:" in backlog
    assert backlog.count("title:") >= 2


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
    for rel in ["README.md", "CONTRIBUTING.md", "ARCHITECTURE.md", "OPERATIONS.md"]:
        content = Path(rel).read_text(encoding="utf-8")
        assert "## Purpose" in content
        assert "## Current State" in content
        assert "## Verification Notes" in content
        assert "## Related Docs" in content
