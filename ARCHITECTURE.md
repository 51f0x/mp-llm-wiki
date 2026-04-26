# LLM Wiki Architecture

## Purpose
Provide a concise technical overview of package structure and workflow boundaries.

## Current State
- Package: `exec_operating_system`.
- Workflows: `ingest.py`, `query.py`, `lint.py`.
- Shared modules include `markdown.py`, `index.py`, `logging_ops.py`, `models.py`, and CLI orchestration in `cli.py`.

## Recommended Improvements
- Expand architecture notes with extension points once docs baseline stabilizes.

## Verification Notes
Cross-check this page against `src/exec_operating_system/*.py` and workflow tests under `tests/`.

## Related Docs
- `docs/README.md`
- `docs/developer/codebase-and-workflows.md`
- `OPERATIONS.md`
