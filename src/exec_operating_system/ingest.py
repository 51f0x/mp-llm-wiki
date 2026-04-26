from __future__ import annotations

from pathlib import Path

from .index import append_index_entry
from .logging_ops import append_log, run_id_now, write_run_file
from .models import IngestResult


def _classify_domain(text: str) -> str:
    lowered = text.lower()
    if "people" in lowered or "hiring" in lowered:
        return "people"
    if "customer" in lowered or "market" in lowered:
        return "customers-market"
    if "execution" in lowered or "project" in lowered:
        return "execution"
    return "strategy"


def _classify_sensitivity(text: str) -> str:
    return "sensitive" if "confidential" in text.lower() else "normal"


def run_ingest(repo_root: Path, source_path: Path) -> IngestResult:
    raw_text = source_path.read_text(encoding="utf-8")
    domain = _classify_domain(raw_text)
    sensitivity = _classify_sensitivity(raw_text)
    run_id = run_id_now()

    page = repo_root / "wiki" / domain / f"{source_path.stem}.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(raw_text, encoding="utf-8")
    page_path = str(page.relative_to(repo_root))

    append_index_entry(repo_root / "ops" / "index.md", f"{source_path.name} -> {page_path}")
    append_log(
        repo_root / "ops" / "log.md",
        f"{run_id} ingest {source_path.name} domain={domain} sensitivity={sensitivity}",
    )
    write_run_file(
        repo_root / "ops" / "runs",
        run_id,
        "ingest",
        (
            f"# Ingest Run {run_id}\n\n"
            f"- source: {source_path}\n"
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
