import random


MIN_NUMBER = 1
MAX_NUMBER = 100
DESCRIPTION = "Find the greatest common divisor of given numbers."


def get_gcd(a, b):
    """returns greatest common divisor of arguments"""

    num1 = a
    num2 = b
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def get_game():
    """returns gcd game data"""

    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = get_gcd(num1, num2)
    question_string = f"{num1} {num2}"
    return (question_string, correct_answer)
