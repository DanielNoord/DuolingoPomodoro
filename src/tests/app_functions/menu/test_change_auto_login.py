import pytest
import rumps
from src.app_functions.menu.change_auto_login import change_auto_login


@pytest.fixture(name="basic_app")
def create_app():
    """Creates a basic app object with some variables to pass to functions

    Returns:
        rumps.App: Basic app
    """
    app = rumps.App("TestApp")
    app.settings = {}
    return app


def test_setting_is_true(mocker, basic_app):
    """Check if setting is changed correctly if True"""
    basic_app.settings["auto_login"] = True
    mock_function = mocker.patch("src.app_functions.menu.change_auto_login.update_menu")
    mocker.patch("src.app_functions.menu.change_auto_login.save_settings")
    change_auto_login(basic_app)
    assert basic_app.settings["auto_login"] is False
    mock_function.assert_called_once_with(basic_app)


def test_setting_is_false(mocker, basic_app):
    """Check if setting is changed correctly if false"""
    basic_app.settings["auto_login"] = False
    mock_function = mocker.patch("src.app_functions.menu.change_auto_login.update_menu")
    mocker.patch("src.app_functions.menu.change_auto_login.save_settings")
    change_auto_login(basic_app)
    assert basic_app.settings["auto_login"] is True
    mock_function.assert_called_once_with(basic_app)
