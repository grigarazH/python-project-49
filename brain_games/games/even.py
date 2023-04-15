import random


MIN_NUMBER = 0
MAX_NUMBER = 100
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game():
    """returns even game data"""

    rand_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = "yes" if rand_num % 2 == 0 else "no"
    question_string = str(rand_num)
    return (question_string, correct_answer)
