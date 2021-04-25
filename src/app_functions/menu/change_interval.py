from src.app_functions.settings.save_settings import save_settings
from src.gui.alert import alert
from src.gui.window import window


def change_interval(app):
    """Change the interval of the global timer that pushes out notifications

    Args:
        app (rumps.App): The App object of the main app
    """
    response = window(
        message="Input new interval for training reminders in seconds",
        dimensions=(200, 50),
    )
    try:
        response = int(response.text)
        app.settings["timer_interval"] = response
        app.global_timer.stop()
        app.global_timer.interval = response
        app.global_timer.start()
        save_settings(app)
    except ValueError:
        retry = alert(
            message="Given value was non-valid\nTry again?",
            ok_button="Yes",
            cancel_button="No",
        )
        if retry:
            change_interval(app)
