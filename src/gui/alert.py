import rumps


def alert(
    title=None, message="", ok_button=None, cancel_button=None, other_button=None
):
    """Creates a rumps.alert with pre-set icon and title

    Args:
        title (str, optional): Title of alert. Defaults to None.
        message (str, optional): Message of alert. Defaults to "".
        ok_button (str, optional): Text of ok button. Defaults to None.
        cancel_button (str, optional): Text of cancel button. Defaults to None.
        other_button (str, optional): Text of other button. Defaults to None.

    Returns:
        int: Number representing the number of the button pressed
    """
    if title:
        title = f"Duolingo Pomodoro\n{title}"
    else:
        title = "Duolingo Pomodoro"
    return rumps.alert(
        title=title,
        message=message,
        ok=ok_button,
        cancel=cancel_button,
        other=other_button,
        icon_path="static/icons/duolingo_icon.png",
    )
