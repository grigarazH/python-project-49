import prompt


def play_game(game):
    """launches a game matching tuple argument"""

    (get_question, get_correct_answer, get_question_string, description) = game
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(description)
    question_count = 3
    i = 0
    while i < question_count:
        question = get_question()
        question_str = get_question_string(question)
        print(f"Question: {question_str}")
        answer = prompt.string("Your answer: ")
        correct_answer = get_correct_answer(question)
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
