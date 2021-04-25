import pytest
import rumps
from src.app_functions.exceptions.login_failed import LoginFailed
from src.app_functions.menu.login_sequence import login


@pytest.fixture(name="basic_app")
def create_app_true():
    """Creates a basic app object with some variables to pass to functions

    Returns:
        rumps.App: Basic app
    """
    app = rumps.App("TestApp")
    app.settings = {"timer_interval": 80}
    app.global_timer = rumps.Timer(None, app.settings["timer_interval"])
    return app


def test_succesfull_login(mocker, basic_app):
    """Check functionality if login succeeds"""
    mock_function1 = mocker.patch("src.app_functions.menu.login_sequence.duolingo_login")
    mock_function2 = mocker.patch("src.app_functions.menu.login_sequence.update_menu")
    mock_function2 = mocker.patch(
        "src.app_functions.menu.login_sequence.get_word_list", return_value={"mela": ["apple"]}
    )
    login(basic_app)
    mock_function1.assert_called_once_with(basic_app)
    mock_function2.assert_called_once_with(basic_app)
    assert basic_app.logged_in is True
    assert basic_app.vocabulary == {"mela": ["apple"]}


def test_failed_login(mocker, basic_app):
    """Check functionality if login fails"""
    mock_function1 = mocker.patch(
        "src.app_functions.menu.login_sequence.duolingo_login", side_effect=LoginFailed
    )
    mock_function2 = mocker.patch("src.app_functions.menu.login_sequence.update_menu")
    login(basic_app)
    mock_function1.assert_called_once_with(basic_app)
    mock_function2.assert_called_once_with(basic_app)
    assert basic_app.logged_in is False
