from src.app_functions.settings.save_settings import save_settings
from src.app_functions.update_menu import update_menu


def change_countdown_statusbar(app):
    """Change setting whether a timer till next notification should be displayed in the menu bar

    Args:
        app (rumps.App): The App object of the main app
    """
    if app.settings["time_in_menu_bar"]:
        app.settings["time_in_menu_bar"] = False
    else:
        app.settings["time_in_menu_bar"] = True
    update_menu(app)
    save_settings(app)
