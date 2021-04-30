from src.app_functions.settings.save_settings import save_settings
from src.app_functions.update_menu import update_menu


def change_strength_level(app, level):
    """Change the credentials to login and then tries to log in with those new credentials
    Currently does not have tests...

    Args:
        app (rumps.App): The App object of the main app
        level (num): The level to change
    """
    if level in app.settings["strength_levels_to_practice"]:
        app.settings["strength_levels_to_practice"].remove(level)
    else:
        app.settings["strength_levels_to_practice"].append(level)
    update_menu(app)
    save_settings(app)
