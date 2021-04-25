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
    question, answer = random.choice(list(app.vocabulary.items()))
    return create_question_prompt(app, question, answer)
