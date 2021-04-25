from src.app_functions.menu.login_sequence import login


def initialize_app(app):
    """Function that will be called when Auto-login is turned on

    Args:
        app (rumps.App): The App object of the main app
    """
    # Login
    login(app)
