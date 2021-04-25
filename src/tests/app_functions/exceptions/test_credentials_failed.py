import pytest
from src.app_functions.exceptions.credentials_failed import \
    CredentialInputFailed


def raise_exception():
    """Raise the exception

    Raises:
        CredentialInputFailed: Test raise
    """
    raise CredentialInputFailed("Credential input failed")


def test_exception():
    """Test throwing of CredentialInputFailed exception"""
    with pytest.raises(CredentialInputFailed, match=r"Credential input failed"):
        raise_exception()
