from src.gui.alert import alert


def show_statistics(app):
    """Creates an alert that displays all statistics of the user

    Args:
        app (rumps.App): The App object of the main app
    """
    message_string = "\n".join(f"{k} {str(i)}" for k, i in app.statistics.values())
    alert(
        title="Statistics",
        message=message_string,
    )
