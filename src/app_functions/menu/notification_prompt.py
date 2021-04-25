import rumps


def notification_prompt(_):
    """Creates the notification in the notification center

    Args:
        _ (rumps.rumps.Timer|rumps.rumps.MenuItem): The timer or menu item that called the function
    """
    rumps.notification(
        title="Time to test some Duolingo!",
        subtitle="",
        message="",
        sound=True,
        icon="static/icons/duolingo_icon.png",
    )
