import json

import rumps
from src.app_functions.exceptions.credentials_failed import CredentialInputFailed
from src.gui.window import window


def input_credentials():
    """Creates a prompt that lets the user input username and input
        If succesful records the data as credentials.json in the Application Support folder

    Raises:
        CredentialInputFailed: If user cancels the action in the username prompt
        CredentialInputFailed: If user cancels the action in the password prompt
    """
    # Get username
    response = window(
        message="Please enter your username", cancel_button=True, dimensions=(200, 50)
    )
    if response.clicked == 0:
        raise CredentialInputFailed
    username = response.text

    # Get password
    response = window(
        message="Please enter your password",
        cancel_button=True,
        dimensions=(200, 50),
    )
    if response.clicked == 0:
        raise CredentialInputFailed
    password = response.text

    # Write new credentials file
    with open(f"{rumps.application_support('Duolingo Pomodoro')}/credentials.json", "w+") as file:
        credential_data = {"username": username, "password": password}
        json.dump(credential_data, file)
