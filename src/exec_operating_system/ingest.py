from __future__ import annotations

from pathlib import Path

from .config import DOMAINS
from .index import append_index_entry
from .logging_ops import append_log, run_id_now, write_run_file
from .markdown import parse_frontmatter
from .models import IngestResult


def _classify_domain(text: str) -> str:
    lowered = text.lower()
    if "people" in lowered or "hiring" in lowered:
        return "people"
    if "customer" in lowered or "market" in lowered:
        return "customers-market"
    if "execution" in lowered or "delivery" in lowered:
        return "execution"
    return "strategy"


def _validated_domain(domain: str) -> str:
    return domain if domain in DOMAINS else "strategy"


def _classify_sensitivity(text: str, frontmatter: dict[str, object]) -> str:
    frontmatter_value = frontmatter.get("sensitivity")
    if isinstance(frontmatter_value, str):
        lowered = frontmatter_value.strip().lower()
        if lowered in {"normal", "sensitive"}:
            return lowered
    return "sensitive" if "confidential" in text.lower() else "normal"


def run_ingest(repo_root: Path, source_path: Path) -> IngestResult:
    raw_text = source_path.read_text(encoding="utf-8")
    frontmatter, _ = parse_frontmatter(raw_text)
    domain = _validated_domain(_classify_domain(raw_text))
    sensitivity = _classify_sensitivity(raw_text, frontmatter)
    run_id = run_id_now()
    ops_dir = repo_root / "ops"
    ops_dir.mkdir(parents=True, exist_ok=True)
    index_file = ops_dir / "index.md"
    log_file = ops_dir / "log.md"
    if not index_file.exists():
        index_file.write_text("# Wiki Index\n", encoding="utf-8")
    if not log_file.exists():
        log_file.write_text("# Operations Log\n", encoding="utf-8")

    page = repo_root / "wiki" / domain / f"{source_path.stem}.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(raw_text, encoding="utf-8")
    page_path = str(page.relative_to(repo_root))
    try:
        source_for_run = str(source_path.relative_to(repo_root))
    except ValueError:
        source_for_run = str(source_path)

    append_index_entry(index_file, f"{source_path.name} -> {page_path}")
    append_log(
        log_file,
        f"{run_id} ingest {source_path.name} domain={domain} sensitivity={sensitivity}",
    )
    write_run_file(
        ops_dir / "runs",
        run_id,
        "ingest",
        (
            f"# Ingest Run {run_id}\n\n"
            f"- source: {source_for_run}\n"
            f"- domain: {domain}\n"
            f"- sensitivity: {sensitivity}\n"
        ),
    )

    return IngestResult(
        run_id=run_id,
        domain=domain,
        sensitivity=sensitivity,
        page_path=page_path,
    )
