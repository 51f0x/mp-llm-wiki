# Contributing to LLM Wiki

## Purpose
Define contribution workflows and quality gates for code and documentation.

## Current State
- Python project configured via `pyproject.toml`.
- Core package is `src/exec_operating_system/`.
- Tests are executed with `pytest`.

## Quality Gates
- Run `pytest -v` before committing.
- Keep docs contract sections accurate when behavior changes.
- Keep root and deep docs discoverable through [Documentation Index](docs/README.md).

## Validation Commands
- `pytest -v`
- `pytest tests/test_docs_navigation.py tests/test_docs_contract.py -v`
- `uv run --extra dev pytest -q`

## Recommended Improvements
- Add CI checks for doc links and metadata contract conformance.

## Verification Notes
Validate workflow and docs gates through tests under `tests/`.

## Related Docs
- [Documentation Index](docs/README.md)
- [README](README.md)
- [Architecture](ARCHITECTURE.md)
