from collections.abc import Callable
from typing import NamedTuple

import prompt

from brain_games.cli import greet_player


class Game(NamedTuple):
    rules: str
    generate_round: Callable[[], tuple[str, str]]
    game_rounds: int


def run(game: Game):
    player_name = greet_player()
    print(game.rules)

    game_result = process_game(game)
    match game_result:
        case True:
            print(f"Congratulations, {player_name}!")
        case False:
            print(f"Let's try again, {player_name}!")


def process_game(game) -> bool:
    for _ in range(game.game_rounds):
        round_question, correct_answer = game.generate_round()
        print(f"Question: {round_question}")

        player_answer = prompt.string("Your answer: ")
        if player_answer != correct_answer:
            print(f"{player_answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            return False

        print('Correct!')

    return True
