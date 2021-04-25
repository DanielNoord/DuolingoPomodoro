from src.duo.get_duolingo_data import get_word_list


def load_vocabulary(app):
    """Reload the vocabulary of the currently logged in user

    Args:
        app (rumps.App): The App object of the main app
    """
    app.vocabulary = get_word_list(app)
