import random


MIN_LENGTH = 5
MAX_LENGTH = 10
PROGRESSION_MIN_STEP = 1
PROGRESSION_MAX_STEP = 10
PROGRESSION_START_MIN = 0
PROGRESSION_START_MAX = 100


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

    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    hidden_index = random.randint(0, length - 1)
    progression = []
    progression_step = random.randint(PROGRESSION_MIN_STEP,
                                      PROGRESSION_MAX_STEP)
    progression_start = random.randint(PROGRESSION_START_MIN,
                                       PROGRESSION_START_MAX)
    progression.append(str(progression_start))
    i = 1
    while i < length:
        progression.append(str(int(progression[i - 1]) + progression_step))
        i += 1
    progression[hidden_index] = ".."
    return " ".join(progression)
