from unittest.mock import mock_open, patch

import pytest
from src.app_functions.statistics.load_statistics import load_statistics


@pytest.fixture(name="statistics")
def statistics_fixture():
    """Creates a basic statistics dict

    Returns:
        dict: Standard statistics dict
    """
    return {
        "total_questions": ["Total questions asked:", 0],
        "correct_answers": ["Correct answers given:", 0],
        "incorrect_answers": ["Incorrect answers given:", 0],
    }


def test_file_present(mocker, statistics):
    """Load if file is present"""
    mocker.patch("json.loads", return_value=statistics)
    with patch("src.app_functions.statistics.load_statistics.open", mock_open()):
        assert load_statistics() == statistics


def test_file_missing(mocker, statistics):
    """Load if file is missing"""
    mocker.patch("json.loads", side_effect=[FileNotFoundError, statistics])
    mock_function = mocker.patch(
        "src.app_functions.statistics.load_statistics.reset_default_statistics"
    )
    with patch("src.app_functions.statistics.load_statistics.open", mock_open()):
        assert load_statistics() == statistics
    mock_function.assert_called_once_with()
