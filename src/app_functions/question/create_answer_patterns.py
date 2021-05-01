import re


def create_answer_patterns(answers):
    """Creates the regex patterns for entries in list of answers

    Args:
        answers (list): The list of possible answers

    Returns:
        list: List of regex patterns based on the possible answers
    """
    patterns = []
    for answer in answers:
        if answer.count("(") != answer.count(")") or "." in answer:
            break
        answer = answer.replace("/", "|").replace("[", "").replace("]", "")
        patterns.append(re.compile(answer + "$"))
    return patterns
