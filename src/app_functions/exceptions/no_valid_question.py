from src.app_functions.exceptions.duolingo_pomodoro import \
    DuolingoPomodoroException


class PickingQuestionFailed(DuolingoPomodoroException):
    """Raised when there are issues with login

    Args:
        DuolingoPomodoroException (Exception): Base excepetion class for app
    """
