import prompt


from brain_games.games.even import get_even_question, get_even_correct_answer
from brain_games.games.calc import get_calc_question, get_calc_correct_answer
from brain_games.games.gcd import get_gcd_question, get_gcd_correct_answer
from brain_games.games.progression import get_progression_question
from brain_games.games.progression import get_progression_correct_answer
from brain_games.games.prime import get_prime_question, get_prime_correct_answer


def print_game_description(game):
    """returns description for chosen game type"""

    if game == "even":
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif game == "calc":
        print("What is the result of the expression?")
    elif game == "gcd":
        print("Find the greatest common divisor of given numbers.")
    elif game == "progression":
        print("What number is missing in the progression?")
    elif game == "prime":
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
    else:
        print("Error")


def get_question(game):
    """returns random question for chosen game type"""

    if game == "even":
        return get_even_question()
    elif game == "calc":
        return get_calc_question()
    elif game == "gcd":
        return get_gcd_question()
    elif game == "progression":
        return get_progression_question()
    elif game == "prime":
        return get_prime_question()


def get_correct_answer(game, question):
    """returns correct answer for chosen game type"""

    if game == "even":
        return get_even_correct_answer(question)
    elif game == "calc":
        return get_calc_correct_answer(question)
    elif game == "gcd":
        return get_gcd_correct_answer(question)
    elif game == "progression":
        return get_progression_correct_answer(question)
    elif game == "prime":
        return get_prime_correct_answer(question)


def play_game(game):
    """launches a game matching string argument"""

    name = ""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print_game_description(game)
    i = 0
    while i < 3:
        question = get_question(game)
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        correct_answer = get_correct_answer(game, question)
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
