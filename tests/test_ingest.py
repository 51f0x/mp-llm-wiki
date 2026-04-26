from pathlib import Path

from exec_operating_system.ingest import run_ingest


def test_ingest_updates_index_log_and_run_artifact(tmp_path: Path):
    (tmp_path / "raw").mkdir()
    source = tmp_path / "raw" / "2026-04-26-board-notes.md"
    source.write_text("strategy: prioritize profitability", encoding="utf-8")

    result = run_ingest(repo_root=tmp_path, source_path=source)

    assert result.domain == "strategy"
    assert result.page_path == "wiki/strategy/2026-04-26-board-notes.md"
    assert len(result.run_id) > 16
    assert result.run_id.endswith("Z")
    assert "2026-04-26-board-notes.md" in (tmp_path / "ops" / "index.md").read_text(encoding="utf-8")
    assert "ingest" in (tmp_path / "ops" / "log.md").read_text(encoding="utf-8")
    assert (tmp_path / "ops" / "runs" / f"{result.run_id}-ingest.md").exists()


def test_ingest_honors_frontmatter_sensitivity(tmp_path: Path):
    (tmp_path / "raw").mkdir()
    source = tmp_path / "raw" / "2026-04-26-comp-plan.md"
    source.write_text(
        "---\n"
        "sensitivity: sensitive\n"
        "---\n"
        "hiring plan updates\n",
        encoding="utf-8",
    )

    result = run_ingest(repo_root=tmp_path, source_path=source)

    assert result.sensitivity == "sensitive"
    run_file = tmp_path / "ops" / "runs" / f"{result.run_id}-ingest.md"
    assert "- sensitivity: sensitive" in run_file.read_text(encoding="utf-8")


def test_ingest_classifies_execution_from_delivery_keyword(tmp_path: Path):
    (tmp_path / "raw").mkdir()
    source = tmp_path / "raw" / "2026-04-26-program-update.md"
    source.write_text("delivery milestone risks", encoding="utf-8")

    result = run_ingest(repo_root=tmp_path, source_path=source)

    assert result.domain == "execution"
    assert result.page_path == "wiki/execution/2026-04-26-program-update.md"
