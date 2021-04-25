import pytest
from src.app_functions.exceptions.login_failed import LoginFailed


def raise_exception():
    """Raise the exception

    Raises:
        LoginFailed: Test raise
    """
    raise LoginFailed("Login failed")


def test_exception():
    """Test throwing of LoginFailed exception"""
    with pytest.raises(LoginFailed, match=r"Login failed"):
        raise_exception()
