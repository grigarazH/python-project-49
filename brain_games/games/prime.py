import random


def get_prime_correct_answer(question):
    """returns correct answer for prime question"""

    PRIME_NUMBERS = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                     41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
                     89, 97, 101, 103, 107, 109, 113, 127, 131,
                     137, 139, 149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223, 227, 229,
                     233, 239, 241, 251, 257, 263, 269, 271)
    return "yes" if int(question) in PRIME_NUMBERS else "no"


def get_prime_question():
    """returns random prime question"""
    min = 0
    max = 271
    return random.randint(min, max)
