from src.gui.alert import alert


def test_call_without_title(mocker):
    """Is the method called with the correct title"""
    mock_func = mocker.patch("rumps.alert")
    alert()
    mock_func.assert_called_with(
        title="Duolingo Pomodoro",
        message="",
        ok=None,
        cancel=None,
        other=None,
        icon_path="static/icons/duolingo_icon.png",
    )


def test_call_with_title(mocker):
    """Is the method called with the correct title"""
    mock_func = mocker.patch("rumps.alert")
    alert(title="Test")
    mock_func.assert_called_with(
        title="Duolingo Pomodoro\nTest",
        message="",
        ok=None,
        cancel=None,
        other=None,
        icon_path="static/icons/duolingo_icon.png",
    )


def test_full_alert(mocker):
    """Is the method called with a full correct alert"""
    mock_func = mocker.patch("rumps.alert")
    alert(
        title="TestTitle",
        message="TestMessage",
        ok_button="TestOK",
        cancel_button="TestCancel",
        other_button="TestOther",
    )
    mock_func.assert_called_with(
        title="Duolingo Pomodoro\nTestTitle",
        message="TestMessage",
        ok="TestOK",
        cancel="TestCancel",
        other="TestOther",
        icon_path="static/icons/duolingo_icon.png",
    )
