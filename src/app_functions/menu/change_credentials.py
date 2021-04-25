from src.app_functions.exceptions.login_failed import LoginFailed
from src.app_functions.update_menu import update_menu
from src.duo.login.duolingo_login import duolingo_login
from src.duo.login.input_credentials import input_credentials


def change_credentials(app):
    """Change the credentials to login and then tries to log in with those new credentials

    Args:
        app (rumps.App): The App object of the main app
    """
    input_credentials()
    # Re-login
    try:
        duolingo_login(app)
        app.logged_in = True
    except LoginFailed:
        app.logged_in = False
    update_menu(app)
