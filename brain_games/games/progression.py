import random


MIN_LENGTH = 5
MAX_LENGTH = 10
PROGRESSION_MIN_STEP = 1
PROGRESSION_MAX_STEP = 10
PROGRESSION_START_MIN = 0
PROGRESSION_START_MAX = 100
DESCRIPTION = "What number is missing in the progression?"


def get_progression(start, step, length):
    progression = []
    progression.append(str(start))
    i = 1
    while i < length:
        progression.append(str(int(progression[i - 1]) + step))
        i += 1
    return progression


def get_question_string(prog, hidden_index):
    """returns progression question string"""

    prog_copy = []
    for i, val in enumerate(prog):
        copy_elem = ".." if i == hidden_index else val
        prog_copy.append(copy_elem)
    return " ".join(prog_copy)


def get_game():
    """returns progression game data"""

    prog_length = random.randint(MIN_LENGTH, MAX_LENGTH)
    hidden_index = random.randint(0, length - 1)
    progression_step = random.randint(PROGRESSION_MIN_STEP,
                                      PROGRESSION_MAX_STEP)
    progression_start = random.randint(PROGRESSION_START_MIN,
                                       PROGRESSION_START_MAX)
    progression = get_progression(progression_start, progression_step, length)
    correct_answer = progression[hidden_index]
    question_string = get_question_string(progression, hidden_index)
    return question_string, correct_answer
