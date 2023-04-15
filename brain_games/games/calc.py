import random

MIN_NUMBER = 0
MAX_NUMBER = 100
DESCRIPTION = "What is the result of the expression?"


def calculate_expression(expression):
    """returns correct answer for calc question"""

    (num1, num2, operator) = expression
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    else:
        return num1 * num2


def get_game():
    """returns calc game data"""

    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(["+", "-", "*"])
    expression = (num1, num2, operator)
    correct_answer = calculate_expression(expression)
    question_string = f"{num1} {operator} {num2}"
    return (question_string, correct_answer)
