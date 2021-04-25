from src.gui.window import window


def test_class_is_called_once(mocker):
    """Is the run method called once"""
    mock_class = mocker.patch("rumps.Window.run")
    window()
    mock_class.assert_called_once_with()


def test_call_with_default_value(mocker):
    """Is the method called with the correct title"""
    mock_class = mocker.patch("rumps.Window")
    window()
    mock_class.assert_called_once_with(
        message="",
        title="Duolingo Pomodoro",
        default_text="",
        ok=None,
        cancel=None,
        dimensions=(320, 160),
        secure=False,
    )


def test_call_with_full_value(mocker):
    """Is the method called with the correct title"""
    mock_class = mocker.patch("rumps.Window")
    window(
        message="TestMessage",
        title="TestTitle",
        default_text="TestText",
        ok_button="TestOK",
        cancel_button="TestCancel",
        dimensions=(400, 150),
        secure=True,
    )
    mock_class.assert_called_once_with(
        message="TestMessage",
        title="Duolingo Pomodoro\nTestTitle",
        default_text="TestText",
        ok="TestOK",
        cancel="TestCancel",
        dimensions=(400, 150),
        secure=True,
    )
