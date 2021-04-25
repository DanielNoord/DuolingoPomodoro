import rumps


def window(
    message="",
    title=None,
    default_text="",
    ok_button=None,
    cancel_button=None,
    dimensions=(320, 160),
    secure=False,
):  # pylint: disable=too-many-arguments
    """Creates a rumps.Window (input prompt) with pre-set icon and title

    Args:
        message (str, optional): Message of window. Defaults to "".
        title (str, optional): Title of window. Defaults to None.
        default_text (str, optional): Default text of input prompt. Defaults to "".
        ok_button (str, optional): Text of ok button. Defaults to None.
        cancel_button (str, optional): Text of cancel button. Defaults to None.
        dimensions (tuple, optional): Dimensions of window. Defaults to (320, 160).
        secure (bool, optional): If the input should be hidden, for passwords. Defaults to False.

    Returns:
        rumps.rumps.Response: Response object containg response on window
    """
    if title:
        title = f"Duolingo Pomodoro\n{title}"
    else:
        title = "Duolingo Pomodoro"
    prompt = rumps.Window(
        message=message,
        title=title,
        default_text=default_text,
        ok=ok_button,
        cancel=cancel_button,
        dimensions=dimensions,
        secure=secure,
    )
    prompt.icon = "static/icons/duolingo_icon.png"
    return prompt.run()
