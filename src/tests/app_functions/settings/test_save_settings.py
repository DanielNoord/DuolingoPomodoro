from unittest.mock import ANY, mock_open, patch

import pytest
import rumps
from src.app_functions.settings.save_settings import save_settings


@pytest.fixture(name="basic_app")
def create_app_true():
    """Creates a basic app object with some variables to pass to functions

    Returns:
        rumps.App: Basic app
    """
    app = rumps.App("TestApp")
    app.settings = {"time_in_menu_bar": False}
    return app


def test_saving(mocker, basic_app):
    """Test if saves correctly"""
    mocker_function = mocker.patch("json.dump")
    with patch("src.app_functions.settings.save_settings.open", mock_open()):
        save_settings(basic_app)
        mocker_function.assert_called_once_with({"time_in_menu_bar": False}, ANY)
