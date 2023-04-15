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

    rand_num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    rand_num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    rand_operator = random.choice(["+", "-", "*"])
    expression = (rand_num1, rand_num2, rand_operator)
    correct_answer = calculate_expression(expression)
    question_string = f"{rand_num1} {rand_operator} {rand_num2}"
    return (question_string, correct_answer)
