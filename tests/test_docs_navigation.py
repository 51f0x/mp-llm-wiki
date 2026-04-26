import re
from pathlib import Path

from tests.docs_inventory import DEEP_DOCS, DOCS_INDEX, ROOT_DOCS

MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)


def _iter_markdown_link_targets(content: str) -> list[str]:
    return [target.strip() for target in MARKDOWN_LINK_RE.findall(content)]


def _split_link_target(target: str) -> tuple[str, str]:
    if "#" not in target:
        return target, ""
    path_part, anchor = target.split("#", 1)
    return path_part, anchor


def _slugify_anchor(heading: str) -> str:
    lowered = heading.strip().lower()
    lowered = re.sub(r"[^\w\s-]", "", lowered)
    return re.sub(r"\s+", "-", lowered)


def _anchors_for_file(path: Path) -> set[str]:
    content = path.read_text(encoding="utf-8")
    return {_slugify_anchor(raw) for raw in HEADING_RE.findall(content)}


def test_root_docs_exist_and_link_docs_index() -> None:
    for path in ROOT_DOCS:
        assert path.exists(), f"missing {path}"
        content = path.read_text(encoding="utf-8")
        links = _iter_markdown_link_targets(content)
        assert (
            "docs/README.md" in links
        ), f"{path} must include markdown link to docs/README.md"


def test_docs_index_links_all_major_sections() -> None:
    assert DOCS_INDEX.exists(), "missing docs/README.md"
    content = DOCS_INDEX.read_text(encoding="utf-8")
    targets = set(_iter_markdown_link_targets(content))
    required = {f"../{path.as_posix()}" for path in ROOT_DOCS} | {
        "executive/strategy-and-value.md",
        "developer/codebase-and-workflows.md",
        "operations/runtime-and-maintenance.md",
        "reference/glossary-and-contracts.md",
        "improvements/documentation-backlog.md",
    }
    missing = required - targets
    assert not missing, f"docs/README.md missing navigation links: {sorted(missing)}"


def test_markdown_relative_links_resolve_for_core_docs() -> None:
    doc_files = [*ROOT_DOCS, DOCS_INDEX, *DEEP_DOCS]
    for path in doc_files:
        content = path.read_text(encoding="utf-8")
        links = _iter_markdown_link_targets(content)
        for raw_target in links:
            if raw_target.startswith(("http://", "https://", "mailto:")):
                continue
            target_path, anchor = _split_link_target(raw_target)
            if target_path.startswith("#"):
                target_path = ""
                anchor = raw_target[1:]
            resolved_path = (path.parent / target_path).resolve() if target_path else path.resolve()
            assert resolved_path.exists(), f"{path} references missing {raw_target}"
            if anchor:
                anchors = _anchors_for_file(resolved_path)
                assert anchor in anchors, f"{path} references missing anchor {raw_target}"
