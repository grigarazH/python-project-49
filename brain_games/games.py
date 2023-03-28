import random
import prompt


def get_even_correct_answer(question):
    """returns correct answer for is even question"""

    return "yes" if int(question) % 2 == 0 else "no"


def get_even_question():
    """returns random is even question"""

    return random.randint(0, 100)


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

    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    operator = random.choice(["+", "-", "*"])
    return f"{num1} {operator} {num2}"


def play_game(game):
    """launches a game matching string argument"""

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    if game == "even":
        print('Answer "yes" if the number is even, otherwise answer "no"')
    elif game == "calc":
        print("What is the result of the expression?")
    else:
        print("Error")
    i = 0
    while i < 3:
        if game == "even":
            question = get_even_question()
        elif game == "calc":
            question = get_calc_question()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if game == "even":
            correct_answer = get_even_correct_answer(question)
        elif game == "calc":
            correct_answer = get_calc_correct_answer(question)
        if str(answer) == str(correct_answer):
            print("Correct!")
        else:
            print((f"'{answer}' is wrong answer ;(. "
                   f"Correct answer was '{correct_answer}'."))
            print(f"Let's try again, {name}!")
            break
        i += 1
    else:
        print(f"Congratulations, {name}!")
