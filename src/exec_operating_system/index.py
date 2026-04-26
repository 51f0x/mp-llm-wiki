from __future__ import annotations

from pathlib import Path


def append_index_entry(index_file: Path, summary: str) -> None:
    with index_file.open("a", encoding="utf-8") as handle:
        handle.write(f"- {summary}\n")
