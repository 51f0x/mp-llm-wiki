import json
from pathlib import Path


def test_golden_question_fixture_has_minimum_coverage():
    data = json.loads(Path("tests/fixtures/golden_questions.json").read_text(encoding="utf-8"))
    domains = {item["domain"] for item in data}
    assert {"strategy", "people", "execution", "customers-market"} <= domains
