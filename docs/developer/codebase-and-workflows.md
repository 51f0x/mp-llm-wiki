audience: developer
last_updated: 2026-04-26
related_docs: [CONTRIBUTING.md, docs/README.md, ARCHITECTURE.md]

# Codebase and Workflows

## Purpose
Explain module boundaries, workflow internals, and testing conventions for contributors.

## Current State
The package exposes ingest/query/lint workflows plus markdown parsing, index updates, models, logging, and CLI orchestration.

## Contributor Workflow
- Run `uv run --extra dev pytest -q` for a full local verification pass.
- Keep `tests/test_docs_navigation.py` and `tests/test_docs_contract.py` in sync with doc structure changes.

## Recommended Improvements
Document extension points for additional lint rules and retrieval strategies.

## Verification Notes
Validate against source modules in `src/exec_operating_system/` and tests under `tests/`.

## Related Docs
- `../../CONTRIBUTING.md`
- `../../ARCHITECTURE.md`
- `../README.md`
