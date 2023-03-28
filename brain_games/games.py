import random
import prompt


def get_even_correct_answer(question):
    """returns correct answer for is even question"""

    return "yes" if int(question) % 2 == 0 else "no"


def get_even_question():
    """returns random is even question"""

    return random.randint(0, 100)


def play_game(game):
    """launches a game matching string argument"""

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    if game == "even":
        print('Answer "yes" if the number is even, otherwise answer "no"')
    else:
        print("Error")
    i = 0
    while i < 3:
        question = get_even_question()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if game == "even":
            correct_answer = get_even_correct_answer(question)
        if answer == correct_answer:
            print("Correct!")
        else:
            print((f"'{answer}' is wrong answer ;(. "
                   f"Correct answer was '{correct_answer}'."))
            print(f"Let's try again, {name}!")
            break
        i += 1
    else:
        print(f"Congratulations, {name}!")
