import json

from rumps import application_support
from src.app_functions.settings.save_settings import save_settings


def get_word_list(app):
    """Get the current vocabulary from the currently loged in user

    Args:
        app (rumps.App): The App object of the main app

    Returns:
        dict: The current vocabulary with word: [translations] pairs
    """
    # Get user info and settings
    user_info = app.lingo.get_user_info()
    if user_info["ui_language"] == "en":
        app.settings["current_target_language"] = "English"
    else:
        app.settings["current_target_language"] = app.lingo.get_language_from_abbr(
            user_info["ui_language"]
        )
    app.settings["current_language_abbr"] = app.lingo.get_abbreviation_of(
        user_info["learning_language_string"]
    )
    save_settings(app)

    # Get vocab
    data = [i for i in app.lingo.get_vocabulary()["vocab_overview"]]
    vocabulary_list = {}
    for i in range(len(data) // 1000 + 1):
        index1 = i * 1000
        index2 = (i + 1) * 1000
        if index2 > len(data) - 1:
            index2 = len(data)

        translations = app.lingo.get_translations(
            [i["word_string"] for i in data[index1:index2]],
            source=app.settings["current_language_abbr"],
            target=user_info["ui_language"],
        )
        strengths = {i["word_string"]: i["strength_bars"] for i in data[index1:index2]}
        for key in translations.keys():
            vocabulary_list[key] = [strengths[key], translations[key]]

    with open(f"{application_support('Duolingo Pomodoro')}/current_vocabulary.json", "w+") as file:
        json.dump(vocabulary_list, file)

    # Perhaps this takes up too much resources. For my personal use-case it seems fine.
    return vocabulary_list
