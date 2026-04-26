# LLM Wiki Design: Full Documentation System (Executive-First)

## Purpose

Define a complete, maintainable documentation system for `llm-wiki` that starts with executive readability while still covering contributor and operator depth. The outcome is a canonical docs baseline that reflects current behavior and includes clearly labeled improvement recommendations.

## Scope and Constraints

- **Primary scope:** Documentation architecture, content model, and validation workflow for the whole repository.
- **Phase focus:** Phase 1 delivers the complete docs set, optimized for executive-first navigation.
- **Recommendation policy:** Include doc-driven improvements when gaps are visible, but explicitly separate them from current-state documentation.
- **Location strategy:** Hybrid layout with key entry docs at repository root and deeper material under `docs/`.
- **Source of truth policy:** Prefer executable truth (code/tests/config) over narrative docs when conflicts appear.

## Documentation Architecture

Use a two-layer structure:

1. **Root layer (entry + trust)**
   - Fast orientation for executives and first-time readers.
   - High-signal pages with clear routing into deeper detail.

2. **`docs/` layer (depth + reference)**
   - Audience-specific and topic-specific detail.
   - Canonical index for discoverability and long-term maintenance.

### Target File Map

- `README.md` - primary executive overview and audience routing.
- `CONTRIBUTING.md` - contribution workflow, quality gates, and standards.
- `ARCHITECTURE.md` - concise technical system overview.
- `OPERATIONS.md` - operational summary and runbook entry point.
- `docs/README.md` - master index and navigation source of truth.
- `docs/executive/` - strategy narrative, value model, and decision-support usage.
- `docs/developer/` - codebase structure, module boundaries, workflow details, testing model.
- `docs/operations/` - setup, runtime workflows, troubleshooting, and recurring maintenance.
- `docs/reference/` - glossary, contracts, schemas, CLI/API references.
- `docs/improvements/` - recommendation documents and backlog for documentation-driven changes.

### Navigation Rules

- Every top-level doc links to `docs/README.md`.
- `docs/README.md` links to all root-level docs and all major `docs/*` sections.
- All deep docs contain a short metadata block with:
  - audience
  - last updated
  - related docs

## Content Contract

Every substantial documentation page should include:

1. **Purpose** - why this page exists and who should read it.
2. **Current state** - present behavior and conventions.
3. **Recommended improvements** (optional) - explicitly marked suggestions.
4. **Verification notes** - how claims can be validated.
5. **Related docs** - links to upstream/downstream context.

This contract keeps pages consistent and makes it easy to distinguish current truth from improvement proposals.

## Documentation Production Workflow

1. **Inventory source facts**
   - Collect from `src/`, tests, configs, scripts, and existing docs/specs/plans.
2. **Extract and normalize**
   - Convert source facts into topic notes (architecture, workflows, operations, contribution, reference).
3. **Draft entry docs**
   - Build or refresh root-level docs for executive-first scanning.
4. **Draft deep docs**
   - Populate `docs/` sections by audience and topic.
5. **Annotate recommendations**
   - Add improvement recommendations only where justified by observed gaps.
6. **Consistency pass**
   - Resolve dead links, contradictory statements, and terminology drift.
7. **Editorial pass**
   - Tighten executive readability while preserving technical fidelity.

## Data Flow

1. Source collection from code and existing docs.
2. Fact extraction into structured notes.
3. Audience shaping into executive and technical artifacts.
4. Cross-linking and indexing via root docs and `docs/README.md`.
5. Quality validation and corrections.
6. Publish as canonical v1 docs baseline.

## Risks and Mitigations

- **Ambiguous implementation behavior**
  - Mark as "current unknown" and add recommendation with explicit assumptions.
- **Conflicting sources**
  - Prioritize code/tests, document discrepancy, and propose alignment action.
- **Scope expansion during writing**
  - Constrain to approved information architecture; defer extra work to improvements backlog.
- **Stale recommendations**
  - Require rationale, expected impact, and date markers for all recommendations.

## Acceptance Criteria

- **Discoverability:** Every doc page is reachable from `README.md` or `docs/README.md`.
- **Consistency:** No unresolved contradictions across architecture, workflow, and operations narratives.
- **Traceability:** Major claims are grounded in code/tests/config/spec evidence.
- **Executive usability:** Top-level docs are scannable in minutes.
- **Contributor operability:** A new contributor can execute core workflows from docs alone.

## Out of Scope

- Implementing behavior changes implied by recommendations.
- Building automated doc generators or publishing pipelines in this phase.
- Redesigning repository architecture unrelated to documentation clarity.

## Open Decisions for Planning Phase

1. Minimum page set for each `docs/*` section in v1.
2. Level of command/output detail in operator runbooks.
3. Convention for recommendation lifecycle tracking (status fields, owners, dates).
4. Link-check and docs-lint enforcement strategy in CI.

---

This design is approved at the concept level and is ready for detailed implementation planning.
