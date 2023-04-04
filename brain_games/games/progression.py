import random


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
