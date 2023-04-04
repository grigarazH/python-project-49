import random


def get_even_correct_answer(question):
    """returns correct answer for is even question"""

    return "yes" if int(question) % 2 == 0 else "no"


def get_even_question():
    """returns random is even question"""

    return random.randint(0, 100)
