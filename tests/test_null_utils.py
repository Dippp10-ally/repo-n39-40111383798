from src.null_utils import coalesce


def test_coalesce_returns_default_for_none():
    assert coalesce(None, 5) == 5


def test_coalesce_preserves_value():
    assert coalesce(0, 5) == 0
