import json

from rumps import application_support


def save_settings(app):
    """Save the settings of the user to settings.json in the Application Support folder

    Args:
        app (rumps.App): The App object of the main app
    """
    with open(f"{application_support('Duolingo Pomodoro')}/settings.json", "w+") as file:
        json.dump(app.settings, file)
