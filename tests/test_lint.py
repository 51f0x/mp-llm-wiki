from pathlib import Path

from exec_operating_system.lint import run_lint


def test_lint_reports_orphan_pages_and_writes_run(tmp_path: Path):
    (tmp_path / "wiki" / "strategy").mkdir(parents=True)
    (tmp_path / "ops" / "runs").mkdir(parents=True)
    (tmp_path / "ops" / "index.md").write_text("- listed -> wiki/strategy/listed.md\n", encoding="utf-8")
    (tmp_path / "ops" / "log.md").write_text("# Operations Log\n", encoding="utf-8")
    (tmp_path / "wiki" / "strategy" / "listed.md").write_text("linked page", encoding="utf-8")
    (tmp_path / "wiki" / "strategy" / "orphan.md").write_text("orphan page", encoding="utf-8")

    result = run_lint(tmp_path)

    assert "wiki/strategy/orphan.md" in result.orphans
    assert (tmp_path / "ops" / "runs" / f"{result.run_id}-lint.md").exists()
