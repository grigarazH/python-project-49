import random

MIN_NUMBER = 0
MAX_NUMBER = 100
DESCRIPTION = "What is the result of the expression?"


def get_calc_correct_answer(question):
    """returns correct answer for calc question"""

    (num1, num2, operator) = question
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    else:
        return num1 * num2


def get_calc_question():
    """returns random calc question"""

    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(["+", "-", "*"])
    return (num1, num2, operator)


def get_calc_question_string(question):
    """returns calc question string"""
    (num1, num2, operator) = question
    return f"{num1} {operator} {num2}"
