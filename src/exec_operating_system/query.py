from __future__ import annotations

from pathlib import Path

from .logging_ops import append_log, run_id_now, write_run_file
from .models import QueryResult


def _first_index_page(index_text: str) -> str:
    for line in index_text.splitlines():
        if "->" not in line:
            continue
        return line.split("->", 1)[1].strip()
    raise ValueError("ops/index.md does not contain a page reference")


def run_query(repo_root: Path, question: str, *, file_to: str, slug: str) -> QueryResult:
    ops_dir = repo_root / "ops"
    index_file = ops_dir / "index.md"
    log_file = ops_dir / "log.md"
    run_id = run_id_now()

    page_path = _first_index_page(index_file.read_text(encoding="utf-8"))
    page_text = (repo_root / page_path).read_text(encoding="utf-8")
    answer = f"Based on {page_path}: {page_text}"

    filed_path = f"wiki/{file_to}/{slug}.md"
    filed = repo_root / filed_path
    filed.parent.mkdir(parents=True, exist_ok=True)
    filed.write_text(
        f"# {slug}\n\n"
        f"Question: {question}\n\n"
        f"{answer}\n",
        encoding="utf-8",
    )

    append_log(log_file, f"{run_id} query filed={filed_path}")
    write_run_file(
        ops_dir / "runs",
        run_id,
        "query",
        (
            f"# Query Run {run_id}\n\n"
            f"- question: {question}\n"
            f"- source: {page_path}\n"
            f"- filed: {filed_path}\n\n"
            f"{answer}\n"
        ),
    )

    return QueryResult(run_id=run_id, answer=answer, filed_path=filed_path)
