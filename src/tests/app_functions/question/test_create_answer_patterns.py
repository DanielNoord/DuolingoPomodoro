import pytest
from src.app_functions.question.create_answer_patterns import create_answer_patterns


@pytest.fixture(name="basic_answer_list")
def create_answers():
    """A basic list of possible answers

    Returns:
        list: List of answer string
    """
    return ["speak", "(he) speaks", "(he/she/it) speaks"]


def test_list_of_answers(basic_answer_list):
    """Check if question is created correctly"""
    patterns = create_answer_patterns(basic_answer_list)
    assert any(regex.match("speak") for regex in patterns)
    assert any(regex.match("he speaks") for regex in patterns)
    assert any(regex.match("she speaks") for regex in patterns)
    assert not any(regex.match("he speak") for regex in patterns)
