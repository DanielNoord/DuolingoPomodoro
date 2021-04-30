from unittest.mock import mock_open, patch

import pytest
import rumps
from src.duo.get_duolingo_data import get_word_list


@pytest.fixture(name="basic_app")
def create_app():
    """Creates a basic app object with some variables to pass to functions

    Returns:
        rumps.App: Basic app
    """

    class Lingo:
        """Simple Class to simulate functions used during data collection"""

        @staticmethod
        def get_user_info():
            """Simulate getting user infor

            Returns:
                dict: User info
            """
            return {
                "learning_language_string": "Italian",
                "username": "kartik",
                "ui_language": "en",
            }

        @staticmethod
        def get_abbreviation_of(_):
            """Simulate getting an abbreviation of a language

            Args:
                _ (str): Full name of language

            Returns:
                str: Abbreviation of Italian
            """
            return "it"

        @staticmethod
        def get_vocabulary():
            """Simulate returning a vocabulary dict

            Returns:
                dict: Vocabulary
            """
            return {
                "vocab_overview": [
                    {
                        "word_string": "a",
                        "strength_bars": 4,
                    }
                ]
            }

        @staticmethod
        def get_translations(_, source, target):  # pylint: disable=unused-argument
            """Simulate getting a translation dict

            Args:
                _ (list): Word list
                source (str): Source language
                target (str): target language

            Returns:
                dict: Translation data
            """
            return {"a": ["to", "at", "in", "for", "into", "on"]}

    app = rumps.App("TestApp")
    app.lingo = Lingo()
    app.settings = {}
    return app


def test_get_vocab(mocker, basic_app):
    """Tests getting the vocabulary list
    Very basic test, might need expanding."""
    mocker.patch("src.duo.get_duolingo_data.save_settings")
    with patch("src.duo.get_duolingo_data.open", mock_open()):
        assert get_word_list(basic_app) == {"a": [4, ["to", "at", "in", "for", "into", "on"]]}
