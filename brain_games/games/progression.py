import random


MIN_LENGTH = 5
MAX_LENGTH = 10
PROGRESSION_MIN_STEP = 1
PROGRESSION_MAX_STEP = 10
PROGRESSION_START_MIN = 0
PROGRESSION_START_MAX = 100
DESCRIPTION = "What number is missing in the progression?"


def get_correct_answer(question):
    """returns correct answer for progression question"""

    (prog, answer_index) = question
    return prog[answer_index]


def get_question():
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
    return (progression, hidden_index)


def get_question_string(question):
    """returns progression question string"""
    
    (prog, hidden_index) = question
    prog_copy = []
    for i, val in enumerate(prog):
        copy_elem = ".." if i == hidden_index else val
        prog_copy.append(copy_elem)
    return " ".join(prog_copy)
