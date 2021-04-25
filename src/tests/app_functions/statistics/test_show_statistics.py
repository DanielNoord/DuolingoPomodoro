import pytest
import rumps
from src.app_functions.statistics.show_statistics import show_statistics


@pytest.fixture(name="basic_app")
def create_app_true():
    """Creates a basic app object with some variables to pass to functions

    Returns:
        rumps.App: Basic app
    """
    app = rumps.App("TestApp")
    app.statistics = {
        "total_questions": ["Total questions asked:", 25],
        "correct_answers": ["Correct answers given:", 15],
        "incorrect_answers": ["Incorrect answers given:", 10],
    }
    return app


def test_saving(mocker, basic_app):
    """Test if saves correctly"""
    mocker_function = mocker.patch("src.app_functions.statistics.show_statistics.alert")
    show_statistics(basic_app)
    mocker_function.assert_called_once_with(
        title="Statistics",
        message="Total questions asked: 25\nCorrect answers given: 15\nIncorrect answers given: 10",
    )
