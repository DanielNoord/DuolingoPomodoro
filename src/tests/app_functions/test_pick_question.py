import pytest
import rumps
from src.app_functions.pick_question import pick_question


@pytest.fixture(name="basic_app")
def create_app():
    """Creates a basic app object with some variables to pass to functions

    Returns:
        rumps.App: Basic app
    """
    app = rumps.App("TestApp")
    app.settings = {
        "strength_levels_to_practice": [1, 2, 3, 4],
    }
    app.vocabulary = {
        "a": [1, ["to", "at", "in", "for", "into", "on"]],
    }
    return app


def test_create_question(mocker, basic_app):
    """Check if question is created correctly"""
    mock_function = mocker.patch("src.app_functions.pick_question.create_question_prompt")
    pick_question(basic_app)
    mock_function.assert_called_once_with(basic_app, "a", ["to", "at", "in", "for", "into", "on"])
