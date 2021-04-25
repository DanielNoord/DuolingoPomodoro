import pytest
import rumps
from src.app_functions.menu.change_countdown_statusbar import change_countdown_statusbar


@pytest.fixture(name="basic_app")
def create_app_true():
    """Creates a basic app object with some variables to pass to functions

    Returns:
        rumps.App: Basic app
    """
    app = rumps.App("TestApp")
    app.settings = {}
    return app


def test_setting_is_true(mocker, basic_app):
    """Check if setting is changed correctly if True"""
    basic_app.settings["time_in_menu_bar"] = True
    mock_function = mocker.patch("src.app_functions.menu.change_countdown_statusbar.update_menu")
    mocker.patch("src.app_functions.menu.change_countdown_statusbar.save_settings")
    change_countdown_statusbar(basic_app)
    assert basic_app.settings["time_in_menu_bar"] is False
    mock_function.assert_called_once_with(basic_app)


def test_setting_is_false(mocker, basic_app):
    """Check if setting is changed correctly if False"""
    basic_app.settings["time_in_menu_bar"] = False
    mock_function = mocker.patch("src.app_functions.menu.change_countdown_statusbar.update_menu")
    mocker.patch("src.app_functions.menu.change_countdown_statusbar.save_settings")
    change_countdown_statusbar(basic_app)
    assert basic_app.settings["time_in_menu_bar"] is True
    mock_function.assert_called_once_with(basic_app)
