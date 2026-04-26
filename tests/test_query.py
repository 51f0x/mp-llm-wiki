from pathlib import Path

from exec_operating_system.query import run_query


def test_query_reads_index_first_and_files_briefing(tmp_path: Path):
    (tmp_path / "wiki" / "strategy").mkdir(parents=True)
    (tmp_path / "wiki" / "briefings").mkdir(parents=True)
    (tmp_path / "ops" / "runs").mkdir(parents=True)
    (tmp_path / "ops" / "index.md").write_text(
        "- revenue-plan -> wiki/strategy/revenue-plan.md\n",
        encoding="utf-8",
    )
    (tmp_path / "ops" / "log.md").write_text("# Operations Log\n", encoding="utf-8")
    (tmp_path / "wiki" / "strategy" / "revenue-plan.md").write_text(
        "Gross margin target is 62% [raw/plan.md]",
        encoding="utf-8",
    )

    result = run_query(
        tmp_path,
        "What is our gross margin target?",
        file_to="briefings",
        slug="gm-target",
    )

    assert "62%" in result.answer
    assert (tmp_path / "wiki" / "briefings" / "gm-target.md").exists()
