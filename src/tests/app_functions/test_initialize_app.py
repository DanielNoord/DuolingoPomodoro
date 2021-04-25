import pytest
import rumps
from src.app_functions.initialize_app import initialize_app


@pytest.fixture(name="basic_app")
def create_app():
    """Creates a basic app object with some variables to pass to functions

    Returns:
        rumps.App: Basic app
    """
    app = rumps.App("TestApp")
    return app


def test_called_correctly(mocker, basic_app):
    """Check if functions are called correctly"""
    mock_function = mocker.patch("src.app_functions.initialize_app.login")
    initialize_app(basic_app)
    mock_function.assert_called_once_with(basic_app)
