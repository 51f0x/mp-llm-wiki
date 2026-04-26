import re
from pathlib import Path

ROOT_DOCS = ["README.md", "CONTRIBUTING.md", "ARCHITECTURE.md", "OPERATIONS.md"]
DOC_FILES = [
    Path("README.md"),
    Path("CONTRIBUTING.md"),
    Path("ARCHITECTURE.md"),
    Path("OPERATIONS.md"),
    Path("docs/README.md"),
    Path("docs/executive/strategy-and-value.md"),
    Path("docs/developer/codebase-and-workflows.md"),
    Path("docs/operations/runtime-and-maintenance.md"),
    Path("docs/reference/glossary-and-contracts.md"),
    Path("docs/improvements/documentation-backlog.md"),
]


def test_root_docs_exist_and_link_docs_index() -> None:
    for rel in ROOT_DOCS:
        path = Path(rel)
        assert path.exists(), f"missing {rel}"
        content = path.read_text(encoding="utf-8")
        assert "docs/README.md" in content, f"{rel} must link docs/README.md"


def test_docs_index_links_all_major_sections() -> None:
    index = Path("docs/README.md")
    assert index.exists(), "missing docs/README.md"
    content = index.read_text(encoding="utf-8")
    required = [
        "README.md",
        "CONTRIBUTING.md",
        "ARCHITECTURE.md",
        "OPERATIONS.md",
        "docs/executive/strategy-and-value.md",
        "docs/developer/codebase-and-workflows.md",
        "docs/operations/runtime-and-maintenance.md",
        "docs/reference/glossary-and-contracts.md",
        "docs/improvements/documentation-backlog.md",
    ]
    for target in required:
        assert target in content, f"missing link target: {target}"


def test_markdown_relative_links_resolve_for_core_docs() -> None:
    for path in DOC_FILES:
        content = path.read_text(encoding="utf-8")
        links = re.findall(r"`([^`]+\.md)`", content)
        for link in links:
            target = (path.parent / link).resolve()
            assert target.exists(), f"{path} references missing {link}"
