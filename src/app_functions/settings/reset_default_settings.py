import json

from rumps import application_support


def reset_default_settings():
    """Called if settings file is missing and then writes settings.json in App Support folder"""
    with open("./static/default_settings.json", "r") as default_file:
        with open(f"{application_support('Duolingo Pomodoro')}/settings.json", "w+") as file:
            json.dump(json.load(default_file), file)
