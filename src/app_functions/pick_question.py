import random

from src.gui.question_prompt import create_question_prompt


def pick_question(app):
    """Function that calls the function to create a question prompt.
    Called by the notification handler

    Args:
        app (rumps.App): The App object of the main app

    Returns:
        bool: True or False depending on whether question was answered successfully
    """
    question_data = [None, None]
    count = 0
    while count < 10:
        question, question_data = random.choice(list(app.vocabulary.items()))
        if question_data[0] in app.settings["strength_levels_to_practice"]:
            return create_question_prompt(app, question, question_data[1])
        count += 1
    raise Exception
