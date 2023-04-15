import random


MIN_NUMBER = 0
MAX_NUMBER = 100
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_even(num):
    """returns yes if num is even, otherwise returns no"""

    return "yes" if num % 2 == 0 else "no"


def get_game():
    """returns even game data"""

    num = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = check_even(num)
    question_string = str(num)
    return (question_string, correct_answer)
