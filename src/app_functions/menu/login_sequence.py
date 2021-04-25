from src.app_functions.exceptions.login_failed import LoginFailed
from src.app_functions.update_menu import update_menu
from src.duo.get_duolingo_data import get_word_list
from src.duo.login.duolingo_login import duolingo_login


def login(app):
    """Re-login with the current set of credentials

    Args:
        app (rumps.App): The App object of the main app
    """
    # Re-login
    try:
        duolingo_login(app)
        app.logged_in = True
        app.vocabulary = get_word_list(app)
        app.global_timer.start()
    except LoginFailed:
        app.logged_in = False
    update_menu(app)
