from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .logging_ops import append_log, run_id_now, write_run_file


@dataclass
class LintResult:
    run_id: str
    orphans: list[str]


def _listed_pages(index_text: str) -> set[str]:
    pages: set[str] = set()
    for line in index_text.splitlines():
        if "->" not in line:
            continue
        pages.add(line.split("->", 1)[1].strip())
    return pages


def run_lint(repo_root: Path) -> LintResult:
    ops_dir = repo_root / "ops"
    index_file = ops_dir / "index.md"
    log_file = ops_dir / "log.md"
    run_id = run_id_now()

    listed_pages = _listed_pages(index_file.read_text(encoding="utf-8"))
    all_pages = {
        page.relative_to(repo_root).as_posix()
        for page in (repo_root / "wiki").glob("**/*.md")
    }
    orphans = sorted(all_pages - listed_pages)

    write_run_file(
        ops_dir / "runs",
        run_id,
        "lint",
        (
            f"# Lint Run {run_id}\n\n"
            f"- orphan_count: {len(orphans)}\n\n"
            "## Orphans\n"
            + "".join(f"- {orphan}\n" for orphan in orphans)
        ),
    )
    append_log(log_file, f"{run_id} lint orphan_count={len(orphans)}")

    return LintResult(run_id=run_id, orphans=orphans)
