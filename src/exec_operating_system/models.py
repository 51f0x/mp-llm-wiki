from __future__ import annotations

from dataclasses import dataclass


@dataclass
class IngestResult:
    run_id: str
    domain: str
    sensitivity: str
    page_path: str
