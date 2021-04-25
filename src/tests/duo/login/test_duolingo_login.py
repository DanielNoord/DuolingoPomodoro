from unittest.mock import mock_open, patch

import duolingo
import pytest
import rumps
from src.app_functions.exceptions.credentials_failed import CredentialInputFailed
from src.app_functions.exceptions.login_failed import LoginFailed
from src.duo.login.duolingo_login import duolingo_login


@pytest.fixture(name="basic_app")
def create_app():
    """Creates a basic app object with some variables to pass to functions

    Returns:
        rumps.App: Basic app
    """
    app = rumps.App("TestApp")
    return app


def test_logging_in(mocker, basic_app):
    """Tests succesfully logging in"""
    mocker.patch("src.duo.login.duolingo_login.duolingo.Duolingo", return_value="TestLingoObject")
    mocker.patch(
        "src.duo.login.duolingo_login.json.load",
    )
    with patch("src.duo.login.duolingo_login.open", mock_open()):
        duolingo_login(basic_app)
    assert basic_app.lingo == "TestLingoObject"


def test_no_credentials_found_cancel(mocker, basic_app):
    """Tests if no credential data is found and the process is cancelled"""
    mocker.patch("src.duo.login.duolingo_login.duolingo.Duolingo", side_effect=FileNotFoundError)
    mocker.patch(
        "src.duo.login.duolingo_login.json.load",
    )
    mocker_function = mocker.patch(
        "src.duo.login.duolingo_login.input_credentials", side_effect=CredentialInputFailed
    )
    with pytest.raises(CredentialInputFailed):
        with patch("src.duo.login.duolingo_login.open", mock_open()):
            duolingo_login(basic_app)
    mocker_function.assert_called_once_with()


def test_no_credentials_found(mocker, basic_app):
    """Tests if no credential data is found"""
    mocker.patch(
        "src.duo.login.duolingo_login.duolingo.Duolingo",
        side_effect=[FileNotFoundError, "TestLingoObject"],
    )
    mocker.patch(
        "src.duo.login.duolingo_login.json.load",
    )
    mocker_function = mocker.patch("src.duo.login.duolingo_login.input_credentials")
    with patch("src.duo.login.duolingo_login.open", mock_open()):
        duolingo_login(basic_app)
    mocker_function.assert_called_once_with()
    assert basic_app.lingo == "TestLingoObject"


def test_login_failed_no_retry(mocker, basic_app):
    """Tests failed login without retry"""
    mocker.patch(
        "src.duo.login.duolingo_login.duolingo.Duolingo",
        side_effect=[duolingo.DuolingoException("Login failed")],
    )
    mocker.patch(
        "src.duo.login.duolingo_login.json.load",
    )
    mocker.patch("src.duo.login.duolingo_login.login_failed", return_value=False)
    with pytest.raises(LoginFailed):
        with patch("src.duo.login.duolingo_login.open", mock_open()):
            duolingo_login(basic_app)


def test_login_failed_retry_fail(mocker, basic_app):
    """Tests failed login with failed retry"""
    mocker.patch(
        "src.duo.login.duolingo_login.duolingo.Duolingo",
        side_effect=[duolingo.DuolingoException("Login failed")],
    )
    mocker.patch(
        "src.duo.login.duolingo_login.json.load",
    )
    mocker.patch("src.duo.login.duolingo_login.login_failed", return_value=True)
    mocker_function = mocker.patch(
        "src.duo.login.duolingo_login.input_credentials", side_effect=CredentialInputFailed
    )
    with pytest.raises(CredentialInputFailed):
        with patch("src.duo.login.duolingo_login.open", mock_open()):
            duolingo_login(basic_app)
    mocker_function.assert_called_once_with()


def test_login_failed_retry_success(mocker, basic_app):
    """Tests failed login with successful retry"""
    mocker.patch(
        "src.duo.login.duolingo_login.duolingo.Duolingo",
        side_effect=[duolingo.DuolingoException("Login failed"), "TestLingoObject"],
    )
    mocker.patch(
        "src.duo.login.duolingo_login.json.load",
    )
    mocker.patch("src.duo.login.duolingo_login.login_failed", return_value=True)
    mocker_function = mocker.patch("src.duo.login.duolingo_login.input_credentials")
    with patch("src.duo.login.duolingo_login.open", mock_open()):
        duolingo_login(basic_app)
    mocker_function.assert_called_once_with()
