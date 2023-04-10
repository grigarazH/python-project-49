#!/usr/bin/env python3

from brain_games.engine import play_game
from brain_games.games.calc import get_calc_question, get_calc_correct_answer
from brain_games.games.calc import get_calc_question_string, DESCRIPTION


def main():
    calc_game = (get_calc_question, get_calc_correct_answer,
            get_calc_question_string, DESCRIPTION)
    play_game(calc_game)


if __name__ == "__main__":
    main()
