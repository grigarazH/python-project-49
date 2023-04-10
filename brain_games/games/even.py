import random


MIN_NUMBER = 0
MAX_NUMBER = 100
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_even_correct_answer(question):
    """returns correct answer for is even question"""

    return "yes" if question % 2 == 0 else "no"


def get_even_question():
    """returns random is even question"""

    return random.randint(MIN_NUMBER, MAX_NUMBER)


def get_even_question_string(question):
    """returns even question string"""

    return str(question)
