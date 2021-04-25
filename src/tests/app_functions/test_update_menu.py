import pytest
import rumps
from src.app_functions.update_menu import update_menu


@pytest.fixture(name="basic_app")
def create_app():
    """Creates a basic app object with some variables to pass to functions

    Returns:
        rumps.App: Basic app
    """
    app = rumps.App("TestApp")
    app.load_vocabulary_wrapper = "SetToVocabWrapper"
    app.settings = {"auto_login": True, "time_in_menu_bar": True}

    def test_callback():
        return None

    app.test_callback = test_callback
    app.menu = [
        rumps.MenuItem("Login to Duolingo", callback=app.test_callback),
        rumps.MenuItem("Reload vocabulary", callback=app.test_callback),
        {
            "Settings": [
                rumps.MenuItem("Auto-login", callback=app.test_callback),
                rumps.MenuItem(
                    "Show countdown in status bar",
                    callback=app.test_callback,
                ),
            ],
        },
    ]
    return app


def test_if_logged_in(basic_app):
    """Check if menu is updated correctly if logged in"""
    basic_app.logged_in = True
    update_menu(basic_app)
    assert basic_app.menu["Reload vocabulary"].callback == "SetToVocabWrapper"
    assert basic_app.menu["Login to Duolingo"].state == 1
    assert basic_app.menu["Settings"]["Auto-login"].state == basic_app.settings["auto_login"]
    assert (
        basic_app.menu["Settings"]["Show countdown in status bar"].state
        == basic_app.settings["time_in_menu_bar"]
    )


def test_if_not_logged_in(basic_app):
    """Check if menu is updated correctly if not logged in"""
    basic_app.logged_in = False
    update_menu(basic_app)
    assert basic_app.menu["Reload vocabulary"].callback is None
    assert basic_app.menu["Login to Duolingo"].state == 0
    assert basic_app.menu["Settings"]["Auto-login"].state == basic_app.settings["auto_login"]
    assert (
        basic_app.menu["Settings"]["Show countdown in status bar"].state
        == basic_app.settings["time_in_menu_bar"]
    )
