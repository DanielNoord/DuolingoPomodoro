from src.app_functions.pick_question import pick_question
from src.app_functions.statistics import save_statistics


def notification_handler(app):
    """Called when clicked on a notification of the app through the decorator of rumps.
    Updates statistics based on return value of pick_question()

    Args:
        app (rumps.App): The App object of the main app
    """
    correct = pick_question(app)
    app.statistics["total_questions"][1] += 1
    if correct:
        app.statistics["correct_answers"][1] += 1
    else:
        app.statistics["incorrect_answers"][1] += 1
    save_statistics.save_statistics(app)
