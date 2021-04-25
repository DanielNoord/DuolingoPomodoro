import json

from rumps import application_support
from src.app_functions.settings.reset_default_settings import reset_default_settings


def load_settings():
    """Load the settings from the Application Support folder

    Returns:
        dict: Dictionary with setting: value pairs
    """
    try:
        with open(f"{application_support('Duolingo Pomodoro')}/settings.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        reset_default_settings()
        with open(f"{application_support('Duolingo Pomodoro')}/settings.json", "r") as file:
            return json.load(file)
