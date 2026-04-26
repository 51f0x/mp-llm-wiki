from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path


def run_id_now() -> str:
    return datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")


def append_log(log_file: Path, line: str) -> None:
    with log_file.open("a", encoding="utf-8") as handle:
        handle.write(f"- {line}\n")


def write_run_file(runs_dir: Path, run_id: str, workflow: str, body: str) -> Path:
    runs_dir.mkdir(parents=True, exist_ok=True)
    run_file = runs_dir / f"{run_id}-{workflow}.md"
    run_file.write_text(body, encoding="utf-8")
    return run_file
