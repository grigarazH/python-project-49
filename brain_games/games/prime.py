import random


PRIME_NUMBERS = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
                 89, 97, 101, 103, 107, 109, 113, 127, 131,
                 137, 139, 149, 151, 157, 163, 167, 173, 179,
                 181, 191, 193, 197, 199, 211, 223, 227, 229,
                 233, 239, 241, 251, 257, 263, 269, 271)
MIN_NUMBER = 0
MAX_NUMBER = 271
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_correct_answer(question):
    """returns correct answer for prime question"""

    return "yes" if question in PRIME_NUMBERS else "no"


def get_question():
    """returns random prime question"""

    return random.randint(MIN_NUMBER, MAX_NUMBER)


def get_question_string(question):
    """returns prime question string"""
    
    return str(question)
