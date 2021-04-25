from src.app_functions.exceptions.duolingo_pomodoro import DuolingoPomodoroException


class CredentialInputFailed(DuolingoPomodoroException):
    """Raised when there are issues with the input of new credentials, mostly when aborted

    Args:
        DuolingoPomodoroException (Exception): Base excpetion class for app
    """
