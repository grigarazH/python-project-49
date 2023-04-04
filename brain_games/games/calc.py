import random


def get_calc_correct_answer(question):
    """returns correct answer for calc question"""

    [num1, operator, num2] = question.split(" ")
    if operator == "+":
        return int(num1) + int(num2)
    elif operator == "-":
        return int(num1) - int(num2)
    else:
        return int(num1) * int(num2)


def get_calc_question():
    """returns random calc question"""
    min = 0
    max = 100
    num1 = random.randint(min, max)
    num2 = random.randint(min, max)
    operator = random.choice(["+", "-", "*"])
    return f"{num1} {operator} {num2}"
