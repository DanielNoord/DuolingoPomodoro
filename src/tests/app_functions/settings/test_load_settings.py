from unittest.mock import mock_open, patch

import pytest
from src.app_functions.settings.load_settings import load_settings


@pytest.fixture(name="settings")
def settings_fixture():
    """Creates a basic settings dict

    Returns:
        dict: Standard settings dict
    """
    return {
        "auto_login": False,
        "current_language": "",
        "timer_interval": 1500,
        "time_in_menu_bar": True,
    }


def test_file_present(mocker, settings):
    """Load if file is present"""
    mocker.patch("json.loads", return_value=settings)
    with patch("src.app_functions.settings.load_settings.open", mock_open()):
        print("Tet")
        assert load_settings() == settings


def test_file_missing(mocker, settings):
    """Load if file is missing"""
    mocker.patch("json.loads", side_effect=[FileNotFoundError, settings])
    mock_function = mocker.patch("src.app_functions.settings.load_settings.reset_default_settings")
    with patch("src.app_functions.settings.load_settings.open", mock_open()):
        assert load_settings() == settings
    mock_function.assert_called_once_with()
