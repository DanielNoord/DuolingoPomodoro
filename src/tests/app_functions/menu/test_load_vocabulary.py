import pytest
import rumps
from src.app_functions.menu.load_vocabulary import load_vocabulary


@pytest.fixture(name="basic_app")
def create_app_true():
    """Creates a basic app object with some variables to pass to functions

    Returns:
        rumps.App: Basic app
    """
    app = rumps.App("TestApp")
    return app


def test_load_vocabulary(mocker, basic_app):
    """Check if vocabulary of app object is set correctly"""
    mock_function = mocker.patch(
        "src.app_functions.menu.load_vocabulary.get_word_list", return_value={"mela": ["apple"]}
    )
    load_vocabulary(basic_app)
    mock_function.assert_called_once_with(basic_app)
    assert basic_app.vocabulary == {"mela": ["apple"]}
