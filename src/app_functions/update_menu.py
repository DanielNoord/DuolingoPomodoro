def update_menu(app):
    """Updates the menu of the app based an a number of variables and settings

    Args:
        app (rumps.App): The App object of the main app
    """
    if app.logged_in:
        app.menu["Reload vocabulary"].set_callback(app.load_vocabulary_wrapper)
        app.menu["Login to Duolingo"].state = True
    else:
        app.menu["Reload vocabulary"].set_callback(None)
        app.menu["Login to Duolingo"].state = False
    app.menu["Settings"]["Auto-login"].state = app.settings["auto_login"]
    app.menu["Settings"]["Show countdown in status bar"].state = app.settings["time_in_menu_bar"]
