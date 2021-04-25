import pytest
import rumps
from src.app_functions.notification_handler import notification_handler


@pytest.fixture(name="basic_app")
def create_app():
    """Creates a basic app object with some variables to pass to functions

    Returns:
        rumps.App: Basic app
    """
    app = rumps.App("TestApp")
    app.statistics = {
        "total_questions": ["Total questions asked:", 0],
        "correct_answers": ["Correct answers given:", 0],
        "incorrect_answers": ["Incorrect answers given:", 0],
    }
    return app


def test_if_question_correct(mocker, basic_app):
    """Check if functions are called correctly if answer is correct"""
    mock_function = mocker.patch(
        "src.app_functions.notification_handler.pick_question", return_value=True
    )
    mock_function2 = mocker.patch(
        "src.app_functions.notification_handler.save_statistics.save_statistics"
    )
    notification_handler(basic_app)
    mock_function.assert_called_once_with(basic_app)
    mock_function2.assert_called_once_with(basic_app)
    assert basic_app.statistics["total_questions"][1] == 1
    assert basic_app.statistics["correct_answers"][1] == 1
    assert basic_app.statistics["incorrect_answers"][1] == 0


def test_if_question_incorrect(mocker, basic_app):
    """Check if functions are called correctly if answer is incorrect"""
    mock_function = mocker.patch(
        "src.app_functions.notification_handler.pick_question", return_value=False
    )
    mock_function2 = mocker.patch(
        "src.app_functions.notification_handler.save_statistics.save_statistics"
    )
    notification_handler(basic_app)
    mock_function.assert_called_once_with(basic_app)
    mock_function2.assert_called_once_with(basic_app)
    assert basic_app.statistics["total_questions"][1] == 1
    assert basic_app.statistics["correct_answers"][1] == 0
    assert basic_app.statistics["incorrect_answers"][1] == 1
