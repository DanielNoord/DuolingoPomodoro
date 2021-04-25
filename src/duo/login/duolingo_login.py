import json

import duolingo
import rumps
from src.app_functions.exceptions.credentials_failed import CredentialInputFailed
from src.app_functions.exceptions.login_failed import LoginFailed
from src.duo.login.input_credentials import (
    input_credentials,
)  # pylint: disable=relative-beyond-top-level
from src.duo.login.login_failed import login_failed  # pylint: disable=relative-beyond-top-level


def duolingo_login(app):
    """Create the Duolingo object based on credential data
    Sets the object as app.lingo

    Args:
        app (rumps.App): The App object of the main app

    Raises:
        CredentialInputFailed: If input of credentials was abrupted
        LoginFailed: If the login failed due to inccorect credentials (or server issues)
    """
    try:
        with open(
            f"{rumps.application_support('Duolingo Pomodoro')}/credentials.json", "r"
        ) as file:
            credential_data = json.load(file)

        app.lingo = duolingo.Duolingo(credential_data["username"], credential_data["password"])
    except FileNotFoundError:
        try:
            input_credentials()
            duolingo_login(app)
        except CredentialInputFailed as err:
            raise CredentialInputFailed from err
    except duolingo.DuolingoException as err:
        if err.args[0] == "Login failed":
            retry = login_failed()
            if retry:
                try:
                    input_credentials()
                    duolingo_login(app)
                except CredentialInputFailed as err:
                    raise CredentialInputFailed from err
            else:
                raise LoginFailed from err
