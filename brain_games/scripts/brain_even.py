#!/usr/bin/env python3


from brain_games.engine import play_game
from brain_games.games.even import get_question, get_correct_answer
from brain_games.games.even import get_question_string, DESCRIPTION


def main():
    game = (get_question, get_correct_answer, get_question_string, DESCRIPTION)
    play_game(game)


if __name__ == "__main__":
    main()
