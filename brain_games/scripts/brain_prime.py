#!/usr/bin/env python3


from brain_games.engine import play_game
from brain_games.games.prime import get_prime_question, get_prime_correct_answer
from brain_games.games.prime import get_prime_question_string, DESCRIPTION


def main():
    game = (get_prime_question, get_prime_correct_answer,
            get_prime_question_string, DESCRIPTION)
    play_game(game)


if __name__ == "__main__":
    main()
