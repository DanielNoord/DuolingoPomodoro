from src.app_functions.settings.save_settings import save_settings
from src.app_functions.update_menu import update_menu


def change_auto_login(app):
    """Change setting whether the app should auto login on start up

    Args:
        app (rumps.App): The App object of the main app
    """
    if app.settings["auto_login"]:
        app.settings["auto_login"] = False
    else:
        app.settings["auto_login"] = True
    update_menu(app)
    save_settings(app)
