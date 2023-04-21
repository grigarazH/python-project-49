import random


MIN_NUMBER = 0
MAX_NUMBER = 100
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_game():
    """returns even game data"""

    rand_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = "yes" if is_even(rand_num) else "no"
    question_string = str(rand_num)
    return question_string, correct_answer
