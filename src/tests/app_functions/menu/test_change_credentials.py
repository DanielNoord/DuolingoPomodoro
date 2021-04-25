import pytest
import rumps
from src.app_functions.exceptions.login_failed import LoginFailed
from src.app_functions.menu.change_credentials import change_credentials


@pytest.fixture(name="basic_app")
def create_app():
    """Creates a basic app object with some variables to pass to functions

    Returns:
        rumps.App: Basic app
    """
    app = rumps.App("TestApp")
    return app


def test_functions_called_correctly_succes(mocker, basic_app):
    """Check functionality if login succeeds"""
    mock_function1 = mocker.patch("src.app_functions.menu.change_credentials.input_credentials")
    mock_function2 = mocker.patch("src.app_functions.menu.change_credentials.duolingo_login")
    mock_function3 = mocker.patch("src.app_functions.menu.change_credentials.update_menu")
    change_credentials(basic_app)
    mock_function1.assert_called_once_with()
    mock_function2.assert_called_once_with(basic_app)
    mock_function3.assert_called_once_with(basic_app)
    assert basic_app.logged_in is True


def test_functions_called_correctly_failure(mocker, basic_app):
    """Check functionality if login fails"""
    mock_function1 = mocker.patch("src.app_functions.menu.change_credentials.input_credentials")
    mock_function2 = mocker.patch(
        "src.app_functions.menu.change_credentials.duolingo_login", side_effect=LoginFailed
    )
    mock_function3 = mocker.patch("src.app_functions.menu.change_credentials.update_menu")
    change_credentials(basic_app)
    mock_function1.assert_called_once_with()
    mock_function2.assert_called_once_with(basic_app)
    mock_function3.assert_called_once_with(basic_app)
    assert basic_app.logged_in is False
