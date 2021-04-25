import json

from rumps import application_support


def reset_default_statistics():
    """Called if stats file is missing and then writes statistics.json in the App Support folder"""
    with open("./static/default_stats.json", "r") as default_file:
        with open(f"{application_support('Duolingo Pomodoro')}/statistics.json", "w+") as file:
            json.dump(json.load(default_file), file)
