from src.app_functions.menu.notification_prompt import notification_prompt


def test_notification(mocker):
    """Check if notification is called correctly"""
    mock_function = mocker.patch("rumps.notification")
    notification_prompt(None)
    mock_function.assert_called_once_with(
        title="Time to test some Duolingo!",
        message="",
        subtitle="",
        sound=True,
        icon="static/icons/duolingo_icon.png",
    )
