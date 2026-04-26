from exec_operating_system.config import DOMAINS, ZONES


def test_domains_and_zones_match_spec():
    assert DOMAINS == [
        "strategy",
        "people",
        "execution",
        "customers-market",
        "decisions",
        "briefings",
    ]
    assert ZONES == ["raw", "wiki", "ops", "schema"]
