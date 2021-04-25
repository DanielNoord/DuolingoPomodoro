from src.app_functions.exceptions.duolingo_pomodoro import \
    DuolingoPomodoroException


class LoginFailed(DuolingoPomodoroException):
    """Raised when there are issues with login

    Args:
        DuolingoPomodoroException (Exception): Base excpetion class for app
    """
