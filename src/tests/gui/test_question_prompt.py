import re
import unittest.mock

import pytest
import rumps
from src.gui.question_prompt import create_question_prompt


@pytest.fixture(name="basic_app")
def create_app():
    """Creates a basic app object with some variables to pass to functions

    Returns:
        rumps.App: Basic app
    """
    app = rumps.App("TestApp")
    app.lingo = object
    app.settings = {"current_target_language": "Italian"}
    return app


def test_incorrect_answer_aborted(mocker, basic_app):
    """Check if abort prompt works"""
    mock_class = unittest.mock.MagicMock()
    mock_class.run = unittest.mock.Mock()
    mock_class.run.side_effect = [
        rumps.rumps.Response(clicked=1, text=""),
        rumps.rumps.Response(clicked=0, text=""),
    ]
    mock_class2 = mocker.patch("rumps.Window", return_value=mock_class)
    assert not create_question_prompt(basic_app, "mela", [re.compile("apple$")])
    assert len(mock_class2.call_args_list) == 2
    mock_class2.assert_called_with(
        message="Translate the above word in Italian",
        title="Duolingo Pomodoro\n\nmela",
        ok="Answer",
        cancel=True,
        dimensions=(320, 100),
    )


def test_incorrect_answer_then_correct(mocker, basic_app):
    """Test if correct answer is found"""
    mock_class = unittest.mock.MagicMock()
    mock_class.run = unittest.mock.Mock()
    mock_class.run.side_effect = [
        rumps.rumps.Response(clicked=1, text=""),
        rumps.rumps.Response(clicked=1, text="appl"),
        rumps.rumps.Response(clicked=1, text="apple"),
    ]
    mock_class2 = mocker.patch("rumps.Window", return_value=mock_class)
    assert create_question_prompt(basic_app, "mela", [re.compile("apple$")])
    assert len(mock_class2.call_args_list) == 3
    mock_class2.assert_called_with(
        message="Translate the above word in Italian",
        title="Duolingo Pomodoro\n\nmela",
        ok="Answer",
        cancel=True,
        dimensions=(320, 100),
    )


def test_incorrect_answer_then_show_then_correct(mocker, basic_app):
    """Test if title shows answer correctly in last prompt"""
    mock_class = unittest.mock.MagicMock()
    mock_class.run = unittest.mock.Mock()
    mock_class.run.side_effect = [
        rumps.rumps.Response(clicked=1, text=""),
        rumps.rumps.Response(clicked=2, text="apple"),
        rumps.rumps.Response(clicked=1, text="apple"),
    ]
    mock_class2 = mocker.patch("rumps.Window", return_value=mock_class)
    assert create_question_prompt(basic_app, "mela", [re.compile("apple$")])
    assert len(mock_class2.call_args_list) == 3
    mock_class2.assert_called_with(
        message="Translate the above word in Italian",
        title="Duolingo Pomodoro\n\nmela\n\nAnswer(s):\napple",
        ok="Answer",
        cancel=True,
        dimensions=(320, 100),
    )
