from unittest.mock import ANY, mock_open, patch

import pytest
import rumps
from src.app_functions.exceptions.credentials_failed import CredentialInputFailed
from src.duo.login.input_credentials import input_credentials


def test_succesful_entry_of_credentials(mocker):
    """Check if prompt correctly returns when to retry"""
    mock_function = mocker.patch(
        "src.duo.login.input_credentials.window",
        side_effect=[rumps.rumps.Response(1, "UserName"), rumps.rumps.Response(1, "Password")],
    )
    mock_function2 = mocker.patch("src.duo.login.input_credentials.json.dump")
    with patch("src.duo.login.input_credentials.open", mock_open()):
        input_credentials()
    mock_function.assert_called_with(
        cancel_button=True, message="Please enter your password", dimensions=(200, 50)
    )
    mock_function2.assert_called_once_with({"username": "UserName", "password": "Password"}, ANY)


def test_stop_during_password(mocker):
    """Check if prompt correctly when broking during password entry"""
    mock_function = mocker.patch(
        "src.duo.login.input_credentials.window",
        side_effect=[rumps.rumps.Response(1, "UserName"), rumps.rumps.Response(0, "Password")],
    )
    with pytest.raises(CredentialInputFailed):
        with patch("src.duo.login.input_credentials.open", mock_open()):
            input_credentials()
    mock_function.assert_called_with(
        cancel_button=True, message="Please enter your password", dimensions=(200, 50)
    )


def test_stop_during_username(mocker):
    """Check if prompt correctly when broking during username entry"""
    mock_function = mocker.patch(
        "src.duo.login.input_credentials.window", side_effect=[rumps.rumps.Response(0, "UserName")]
    )
    with pytest.raises(CredentialInputFailed):
        with patch("src.duo.login.input_credentials.open", mock_open()):
            input_credentials()
    mock_function.assert_called_once_with(
        cancel_button=True, message="Please enter your username", dimensions=(200, 50)
    )
