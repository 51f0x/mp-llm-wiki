# Policy contract

- **Raw zone immutability:** Content in the `raw` zone is immutable after capture; corrections happen in downstream zones, not by rewriting raw source material.
- **Append-only `ops/log.md`:** The operations log is append-only; do not delete or rewrite past entries. Add new lines for new events.
- **Run artifacts in `ops/runs/`:** Per-run outputs, exports, and scratch artifacts belong under `ops/runs/` (or a similar run-scoped path), not in canonical wiki or policy paths.
- **Citation mode: balanced:** Prefer balanced citation—link to sources and context without over- or under-citing; default stance is traceability without noise.
- **Sensitive updates rationale:** When updating sensitive or high-impact content, document the rationale (what changed, why, and any review or approval) in the appropriate log or run notes.
