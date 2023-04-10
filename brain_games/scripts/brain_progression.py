#!/usr/bin/env python3


from brain_games.engine import play_game
from brain_games.games.progression import get_progression_question
from brain_games.games.progression import get_progression_correct_answer
from brain_games.games.progression import get_progression_question_string
from brain_games.games.progression import DESCRIPTION


def main():
    game = (get_progression_question, get_progression_correct_answer,
            get_progression_question_string, DESCRIPTION)
    play_game(game)


if __name__ == "__main__":
    main()
