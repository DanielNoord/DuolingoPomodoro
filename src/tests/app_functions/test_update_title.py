import pytest
import rumps
from src.app_functions.update_title import update_title_bar


@pytest.fixture(name="basic_app")
def create_app():
    """Creates a basic app object with some variables to pass to functions

    Returns:
        rumps.App: Basic app
    """
    app = rumps.App("TestApp")
    app.title = None
    app.global_timer = rumps.Timer(None, 100)
    app.global_timer.start()
    return app


def test_updated_not_login(basic_app):
    """Check if title is correctly displayed if not logged in"""
    basic_app.settings = {"time_in_menu_bar": True}
    basic_app.logged_in = False
    update_title_bar(basic_app)
    assert basic_app.title == "(X)"


def test_updated_logged_in(basic_app):
    """Check if title is correctly displayed if logged in"""
    basic_app.settings = {
        "time_in_menu_bar": True,
        "timer_interval": 100,
    }
    basic_app.logged_in = True
    update_title_bar(basic_app)
    assert basic_app.title == "(01:39)"


def test_toggle_off(basic_app):
    """Check if title is correctly displayed if the toggle is turned off"""
    basic_app.settings = {"time_in_menu_bar": False}
    update_title_bar(basic_app)
    assert basic_app.title is None
