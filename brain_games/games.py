import random
import prompt


PRIME_NUMBERS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
                89, 97, 101, 103, 107, 109, 113, 127, 131, 
                137, 139, 149, 151, 157, 163, 167, 173, 179, 
                181, 191, 193, 197, 199, 211, 223, 227, 229, 
                233, 239, 241, 251, 257, 263, 269, 271]



def print_game_description(game):
    """returns description for chosen game type"""

    if game == "even":
        print('Answer "yes" if the number is even, otherwise answer "no"')
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

    [num1, num2] = question.split(" ")
    return get_gcd(int(num1), int(num2))


def get_gcd_question():
    """returns random gcd question"""

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return f"{num1} {num2}"


def get_progression_correct_answer(question):
    """returns correct answer for progression question"""

    prog = question.split(" ")
    for (index, item) in enumerate(prog):
        if item == "..":
            answer_index = index
    if answer_index == 0:
        return int(prog[1]) - (int(prog[2]) - int(prog[1]))
    if answer_index == 1:
        return int(prog[0]) + (int(prog[3]) - int(prog[2]))
    else:
        return int(prog[answer_index - 1]) + (int(prog[1]) - int(prog[0]))


def get_progression_question():
    """returns random progression question"""

    length = random.randint(5, 10)
    hidden_index = random.randint(0, length - 1)
    progression = []
    progression_step = random.randint(1, 10)
    progression.append(str(random.randint(0, 100)))
    i = 1
    while i < length:
        progression.append(str(int(progression[i - 1]) + progression_step))
        i += 1
    progression[hidden_index] = ".."
    return " ".join(progression)



def get_prime_correct_answer(question):
    """returns correct answer for prime question"""

    return "yes" if int(question) in PRIME_NUMBERS else "no"


def get_prime_question():
    """returns random prime question"""

    return random.randint(0, 271)


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
