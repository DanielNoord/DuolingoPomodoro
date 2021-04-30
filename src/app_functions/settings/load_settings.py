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
            current_settings = json.load(file)
            with open("./static/default_settings.json", "r") as default_file:
                default_settings = json.load(default_file)
                for def_key, def_value in default_settings.items():
                    if def_key not in current_settings:
                        current_settings[def_key] = def_value
        return current_settings
    except FileNotFoundError:
        reset_default_settings()
        with open(f"{application_support('Duolingo Pomodoro')}/settings.json", "r") as file:
            return json.load(file)
