import random


MIN_NUMBER = 0
MAX_NUMBER = 500
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    i = 2
    while i < number:
        if number % i == 0:
            return False
        i += 1
    return True


def get_game():
    """returns prime game data"""

    rand_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = "yes" if is_prime(rand_num) else "no"
    question_string = str(rand_num)
    return question_string, correct_answer
