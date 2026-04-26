import subprocess
from pathlib import Path


def test_ingest_command_creates_run_artifact(tmp_path: Path):
    raw = tmp_path / "raw"
    raw.mkdir()
    (tmp_path / "ops" / "runs").mkdir(parents=True)
    (tmp_path / "ops" / "index.md").write_text("# Wiki Index\n", encoding="utf-8")
    (tmp_path / "ops" / "log.md").write_text("# Operations Log\n", encoding="utf-8")
    src = raw / "leadership-update.md"
    src.write_text("strategy update", encoding="utf-8")
    result = subprocess.run(
        ["python", "-m", "exec_operating_system.cli", "ingest", str(tmp_path), str(src)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert any((tmp_path / "ops" / "runs").glob("*-ingest.md"))
