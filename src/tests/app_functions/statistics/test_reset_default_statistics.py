from unittest.mock import ANY, patch

from src.app_functions.statistics.reset_default_statistics import reset_default_statistics


def test_reset_correctly(mocker):
    """Test if data is rest correctly"""
    mocker_function = mocker.patch("json.dump")

    with patch(
        "src.app_functions.statistics.reset_default_statistics.open",
        side_effect=[
            open("src/tests/app_functions/statistics/test_stats.json"),
            open("src/tests/app_functions/statistics/test_stats.json"),
        ],
    ):
        reset_default_statistics()
        mocker_function.assert_called_once_with(
            {
                "total_questions": ["Total questions asked:", 0],
                "correct_answers": ["Correct answers given:", 0],
                "incorrect_answers": ["Incorrect answers given:", 0],
            },
            ANY,
        )
