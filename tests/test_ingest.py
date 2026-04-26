from pathlib import Path

from exec_operating_system.ingest import run_ingest


def test_ingest_updates_index_log_and_run_artifact(tmp_path: Path):
    (tmp_path / "raw").mkdir()
    (tmp_path / "wiki" / "strategy").mkdir(parents=True)
    (tmp_path / "ops" / "runs").mkdir(parents=True)
    (tmp_path / "ops" / "index.md").write_text("# Wiki Index\n", encoding="utf-8")
    (tmp_path / "ops" / "log.md").write_text("# Operations Log\n", encoding="utf-8")
    source = tmp_path / "raw" / "2026-04-26-board-notes.md"
    source.write_text("strategy: prioritize profitability", encoding="utf-8")

    result = run_ingest(repo_root=tmp_path, source_path=source)

    assert result.domain == "strategy"
    assert "2026-04-26-board-notes.md" in (tmp_path / "ops" / "index.md").read_text(encoding="utf-8")
    assert "ingest" in (tmp_path / "ops" / "log.md").read_text(encoding="utf-8")
    assert (tmp_path / "ops" / "runs" / f"{result.run_id}-ingest.md").exists()
