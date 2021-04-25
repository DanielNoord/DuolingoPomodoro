from unittest.mock import ANY, patch

from src.app_functions.settings.reset_default_settings import reset_default_settings


def test_reset_correctly(mocker):
    """Test if data is rest correctly"""
    mocker_function = mocker.patch("json.dump")

    with patch(
        "src.app_functions.settings.reset_default_settings.open",
        side_effect=[
            open("src/tests/app_functions/settings/test_settings.json"),
            open("src/tests/app_functions/settings/test_settings.json"),
        ],
    ):
        reset_default_settings()
        mocker_function.assert_called_once_with(
            {
                "auto_login": False,
                "current_language": "",
                "timer_interval": 1500,
                "time_in_menu_bar": True,
            },
            ANY,
        )
