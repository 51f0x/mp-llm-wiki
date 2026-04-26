# LLM Wiki Design: Executive Operating System (Topic-Centric)

## Purpose

Design a leadership-focused "second brain" using the LLM Wiki pattern. The system continuously ingests work artifacts, maintains a topic-centric markdown wiki, and supports faster decisions, better alignment, and durable institutional memory.

This spec defines the first sub-project only: `exec_operating_system`.

## Scope and Constraints

- **Primary scope:** Executive Operating System for company leadership topics.
- **Outcome priority:** Balanced across decision velocity, alignment, memory, and coaching utility.
- **Data breadth target:** Broad company-relevant inputs over time, phased through controlled onboarding.
- **Sensitivity model:** `hybrid_controlled` (local wiki with selected imports and strict controls).
- **Write policy:** `full_autowrite_with_audit` (LLM writes directly, all actions logged).
- **Citation policy:** `balanced` (factual claims cite sources; synthesis may be uncited but linked to supporting pages).

## Architecture

The system uses four top-level zones:

1. `raw/`  
   Immutable source artifacts. LLM reads but never edits this layer.

2. `wiki/`  
   LLM-maintained markdown knowledge base with domain-first organization.

3. `ops/`  
   Operational files for navigation, auditability, and run history.

4. `schema/`  
   Agent behavior contract defining rules, workflows, and conventions.

### Topic-Centric Wiki Layout

`wiki/` is organized by leadership domains:

- `wiki/strategy/`
- `wiki/people/`
- `wiki/execution/`
- `wiki/customers-market/`
- `wiki/decisions/` (cross-domain decision records)
- `wiki/briefings/` (reusable generated outputs)

### Cross-Linking Rules

- Domain pages should link to relevant pages in at least one other domain when applicable.
- Decision pages are anchor artifacts and should be referenced from impacted domain pages.
- `ops/index.md` is the primary machine-friendly + human-friendly navigation map.

## Core Workflows

### Ingest Workflow

1. New source is added to `raw/`.
2. LLM classifies source by:
   - domain (`strategy|people|execution|customers-market|multi-domain`)
   - sensitivity (`normal|sensitive`)
3. LLM auto-updates and/or creates impacted pages under `wiki/`.
4. LLM always updates:
   - `ops/index.md` (catalog and short summaries)
   - `ops/log.md` (append-only operation timeline)
   - `ops/runs/<timestamp>-ingest.md` (detailed operation report)
5. Sensitive updates remain auto-written but must include explicit metadata tags and classification rationale in run reports.

### Query Workflow

1. LLM reads `ops/index.md` first to shortlist relevant pages.
2. LLM synthesizes answers from wiki pages:
   - factual/attributable claims include citations
   - strategic synthesis may omit direct citation if it links to supporting wiki pages
3. Valuable outputs can be filed back into the wiki:
   - `wiki/briefings/` for recurring decision-support summaries
   - `wiki/decisions/` for formalized decision artifacts
4. Every filed query output is recorded in `ops/log.md` and a run file in `ops/runs/`.

### Lint Workflow

Periodic lint passes (recommended weekly) should:

- detect contradiction or drift across pages
- detect orphan pages (no inbound links)
- flag weakly-supported high-impact claims
- identify missing pages for recurring entities/themes
- recommend follow-up sources or research questions

Output is written to `ops/runs/<timestamp>-lint.md`. Safe fixes may be auto-applied and logged.

## Safeguards and Controls

### Source and Integration Control

- Only allowlisted connectors/feeds can add to `raw/`.
- Imported external content must preserve source identity and ingestion timestamp.

### Data Safety and Traceability

- LLM must never edit files under `raw/`.
- Every operation must emit:
  - a concise entry in `ops/log.md`
  - a detailed run artifact in `ops/runs/`
- Contradictions are handled by explicit supersession notes (for example `changed_on`, `superseded_by`) rather than silent rewrites.

## Page Metadata Standard

### Standard Wiki Page Frontmatter

- `title`
- `domain`
- `last_updated`
- `source_refs`
- `confidence` (`low|medium|high`)
- `sensitivity`
- `related_pages`

### Decision Page Frontmatter (`wiki/decisions/`)

- `decision_id`
- `status` (`proposed|active|revisited|superseded`)
- `context`
- `options_considered`
- `rationale`
- `impact_areas`

## Verification Strategy (v1)

1. Build a representative ingest test set across the four domains.
2. Define a golden question set for core leadership use cases.
3. Evaluate answer quality, citation behavior, and retrieval speed.
4. Re-run selected goldens weekly to detect drift.
5. Verify sensitive artifacts are tagged and auditable.
6. Confirm each operation is reconstructable via `ops/log.md`, `ops/runs/*`, and git history.

## Out of Scope (v1)

- Full company-wide connector automation with no curation gates.
- Advanced semantic retrieval infrastructure (keep index-first behavior initially).
- Broad role-based access control system beyond sensitivity tagging conventions.
- Fully autonomous external web research loops.

## Open Decisions for Planning Phase

1. Initial connector list and ingestion cadence.
2. Domain page templates for each top-level topic.
3. Sensitive-content taxonomy and review ritual.
4. Golden question set and acceptance thresholds.
5. Trigger model for lint runs (time-based vs event-based).

---

This design is approved at the concept level and is ready to translate into an implementation plan.
