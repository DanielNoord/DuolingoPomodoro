import pytest
import rumps
from src.app_functions.menu.change_interval import change_interval


@pytest.fixture(name="basic_app")
def create_app_true():
    """Creates a basic app object with some variables to pass to functions

    Returns:
        rumps.App: Basic app
    """
    app = rumps.App("TestApp")
    app.settings = {"timer_interval": 100}
    app.global_timer = rumps.Timer(None, app.settings["timer_interval"])
    return app


def test_correct_value(mocker, basic_app):
    """Check if setting is changed correctly if correct value is supplied"""
    mock_function = mocker.patch(
        "src.app_functions.menu.change_interval.window",
        return_value=rumps.rumps.Response(None, 150),
    )
    mock_function2 = mocker.patch("src.app_functions.menu.change_interval.save_settings")
    change_interval(basic_app)
    assert basic_app.settings["timer_interval"] == 150
    assert basic_app.global_timer.interval == 150
    mock_function.assert_called_once_with(
        message="Input new interval for training reminders in seconds",
        dimensions=(200, 50),
    )
    mock_function2.assert_called_once_with(basic_app)


def test_inccorrect_value_retry(mocker, basic_app):
    """Check if setting is handled correctly if incorrect value is supplied and retried"""
    mock_function = mocker.patch(
        "src.app_functions.menu.change_interval.window",
        side_effect=[
            rumps.rumps.Response(None, "Fifteen"),
            rumps.rumps.Response(None, 200),
        ],
    )
    mock_function2 = mocker.patch("src.app_functions.menu.change_interval.save_settings")
    mocker.patch("src.app_functions.menu.change_interval.alert", return_value=True)
    change_interval(basic_app)
    assert basic_app.settings["timer_interval"] == 200
    assert basic_app.global_timer.interval == 200
    mock_function.assert_called_with(
        message="Input new interval for training reminders in seconds",
        dimensions=(200, 50),
    )
    mock_function2.assert_called_once_with(basic_app)


def test_inccorrect_value_no_retry(mocker, basic_app):
    """Check if setting is handled correctly if incorrect value is supplied without retry"""
    mock_function = mocker.patch(
        "src.app_functions.menu.change_interval.window",
        return_value=rumps.rumps.Response(None, "Fifteen"),
    )
    mocker.patch("src.app_functions.menu.change_interval.alert", return_value=False)
    change_interval(basic_app)
    assert basic_app.settings["timer_interval"] == 100
    assert basic_app.global_timer.interval == 100
    mock_function.assert_called_once_with(
        message="Input new interval for training reminders in seconds",
        dimensions=(200, 50),
    )
