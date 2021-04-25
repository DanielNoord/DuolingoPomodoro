import json

from rumps import application_support


def save_statistics(app):
    """Save the statistics of the user to statistics.json in the Application Support folder

    Args:
        app (rumps.App): The App object of the main app
    """
    with open(f"{application_support('Duolingo Pomodoro')}/statistics.json", "w+") as file:
        json.dump(app.statistics, file)
