from src.duo.login.login_failed import login_failed


def test_want_to_retry(mocker):
    """Check if prompt correctly returns when to retry"""
    mock_function = mocker.patch("src.duo.login.login_failed.alert", return_value=1)
    assert login_failed() is True
    mock_function.assert_called_once_with(
        cancel_button=True, message="Login failed", ok_button="Retry"
    )


def test_want_no_retry(mocker):
    """Check if prompt correctly returns when not to retry"""
    mock_function = mocker.patch("src.duo.login.login_failed.alert", return_value=0)
    assert login_failed() is False
    mock_function.assert_called_once_with(
        cancel_button=True, message="Login failed", ok_button="Retry"
    )
