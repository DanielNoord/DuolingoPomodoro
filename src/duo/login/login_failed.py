from src.gui.alert import alert


def login_failed():
    """Creates an alert to notify user that logged in failed and whether user wants to try again

    Returns:
        bool: Whether the users wants to retry
    """
    # Get username
    prompt = alert(
        message="Login failed",
        ok_button="Retry",
        cancel_button=True,
    )
    if prompt == 0:
        return False
    return True
