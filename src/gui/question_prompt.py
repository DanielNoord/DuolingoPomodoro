import rumps


def create_question_prompt(app, question, answers, incorrect=False, show_answer=False):
    """Creates the window for a duolingo question

    Args:
        app (rumps.App): The App object of the main app
        question (str): The question-word
        answers (list): List of regex pattern answers
        incorrect (bool, optional): Whether a previous answer was incorrect. Defaults to False.
        show_answer (bool, optional): Whether the window should display answers. Defaults to False.

    Returns:
        bool: True or False depending on whether question was answered successfully
    """
    prompt = rumps.Window(
        message=f"Translate the above word in {app.settings['current_target_language']}",
        title="Duolingo Pomodoro\n\n" f"{question}",
        ok="Answer",
        cancel=True,
        dimensions=(320, 100),
    )
    if incorrect:
        prompt.title += "\n\nIncorrect"
    if show_answer is False:
        prompt.add_button("Show answer")
    prompt.icon = "static/icons/duolingo_icon.png"
    response = prompt.run()

    # Clicked "Answer" button
    if response.clicked == 1:
        if not any(regex.match(response.text) for regex in answers):
            return create_question_prompt(app, question, answers, True)
        return True
    # Clicked "Cancel" button
    if response.clicked == 0:
        return False
    # Clicked "Show answer" button
    answer_string = "\n".join(i.pattern[:-1].replace("|", "/") for i in answers)
    return create_question_prompt(
        app, f"{question}\n\nAnswer(s):\n{answer_string}", answers, show_answer=True
    )
