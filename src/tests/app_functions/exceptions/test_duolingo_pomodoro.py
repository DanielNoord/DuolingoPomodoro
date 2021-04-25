import pytest
from src.app_functions.exceptions.duolingo_pomodoro import \
    DuolingoPomodoroException


def raise_exception():
    """Raise the exception

    Raises:
        DuolingoPomodoroException: Test raise
    """
    raise DuolingoPomodoroException("Test")


def test_exception():
    """Test throwing of DuolingoPomodoroException exception"""
    with pytest.raises(DuolingoPomodoroException, match=r"Test"):
        raise_exception()
