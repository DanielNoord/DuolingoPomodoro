from unittest.mock import ANY, mock_open, patch

import pytest
import rumps
from src.app_functions.statistics.save_statistics import save_statistics


@pytest.fixture(name="basic_app")
def create_app_true():
    """Creates a basic app object with some variables to pass to functions

    Returns:
        rumps.App: Basic app
    """
    app = rumps.App("TestApp")
    app.statistics = {"total_questions": ["Total questions asked:", 0]}
    return app


def test_saving(mocker, basic_app):
    """Test if saves correctly"""
    mocker_function = mocker.patch("json.dump")
    with patch("src.app_functions.statistics.save_statistics.open", mock_open()):
        save_statistics(basic_app)
        mocker_function.assert_called_once_with(
            {"total_questions": ["Total questions asked:", 0]}, ANY
        )
