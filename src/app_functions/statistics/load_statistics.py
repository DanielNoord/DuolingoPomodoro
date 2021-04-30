import json

from rumps import application_support
from src.app_functions.statistics.reset_default_statistics import reset_default_statistics


def load_statistics():
    """Load the statistics from the Application Support folder

    Returns:
        dict: Dictionary with stat: [display_name, value] pairs
    """
    try:
        with open(f"{application_support('Duolingo Pomodoro')}/statistics.json", "r") as file:
            current_statistics = json.load(file)
            with open("./static/default_statistics.json", "r") as default_file:
                default_statistics = json.load(default_file)
                for def_key, def_value in default_statistics.items():
                    if def_key not in current_statistics:
                        current_statistics[def_key] = def_value
            return current_statistics
    except FileNotFoundError:
        reset_default_statistics()
        with open(f"{application_support('Duolingo Pomodoro')}/statistics.json", "r") as file:
            return json.load(file)
