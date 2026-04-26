# LLM Wiki Operations

## Purpose
Route operators to setup, runtime workflows, and troubleshooting paths.

## Current State
- CLI commands are exposed by `python -m exec_operating_system.cli`.
- Runs write logs and artifacts under `ops/log.md`, `ops/index.md`, and `ops/runs/`.

## Runtime Workflow Entry Points
- Ingest flow: `python -m exec_operating_system.cli ingest <repo_root> <source_path>`
- Query flow: `python -m exec_operating_system.cli query <repo_root> "<question>" --slug <slug> --file-to briefings`
- Lint flow: `python -m exec_operating_system.cli lint <repo_root>`
- Deep runbook details: `docs/operations/runtime-and-maintenance.md`

## Recommended Improvements
- Add standardized runbook templates for recurring maintenance routines.

## Verification Notes
Operational behavior is implemented in `src/exec_operating_system/cli.py`, `src/exec_operating_system/logging_ops.py`, and validated by tests under `tests/`.

## Related Docs
- `docs/README.md`
- `docs/operations/runtime-and-maintenance.md`
- `README.md`
