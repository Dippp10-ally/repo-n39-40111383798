"""Helpers for None-safe operations."""


def coalesce(value, default=None):
    """Return the default when value is None."""
    return default if value is None else value
