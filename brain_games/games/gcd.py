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


def get_gcd_correct_answer(question):
    """returns correct answer for gcd question"""

    (num1, num2) = question
    return get_gcd(num1, num2)


def get_gcd_question():
    """returns random gcd question"""

    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    return (num1, num2)


def get_gcd_question_string(question):
    """returns gcd question string"""

    (num1, num2) = question
    return f"{num1} {num2}"
