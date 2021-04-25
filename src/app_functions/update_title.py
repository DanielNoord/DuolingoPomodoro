import time


def update_title_bar(app):
    """Updates the name of the app in the menu bar (the text next to the icon)

    Args:
        app (rumps.App): The App object of the main app
    """
    if app.settings["time_in_menu_bar"]:
        if not app.logged_in:
            app.title = "(X)"
        else:
            time_left = (
                app.global_timer._nsdate.timeIntervalSinceNow()  # pylint: disable=protected-access
                % app.settings["timer_interval"]
            )
            app.title = f"({time.strftime('%M:%S', time.gmtime(time_left))})"
    else:
        app.title = None
