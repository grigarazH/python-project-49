import prompt


def play_game(game):
    """launches a game matching argument"""

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.DESCRIPTION)
    question_count = 3
    i = 0
    while i < question_count:
        (question_string, correct_answer) = game.get_game()
        print(f"Question: {question_string}")
        answer = prompt.string("Your answer: ")
        if str(answer) == str(correct_answer):
            print("Correct!")
        else:
            print((f"'{answer}' is wrong answer ;(. "
                   f"Correct answer was '{correct_answer}'."))
            print(f"Let's try again, {name}!")
            return
        i += 1
    print(f"Congratulations, {name}!")
