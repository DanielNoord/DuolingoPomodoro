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
            return json.load(file)
    except FileNotFoundError:
        reset_default_statistics()
        with open(f"{application_support('Duolingo Pomodoro')}/statistics.json", "r") as file:
            return json.load(file)
