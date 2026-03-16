import random

from brain_games.games.engine import Game, run

MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_round() -> tuple[str, str]:
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    answer = 'yes' if question % 2 == 0 else 'no'
    return str(question), answer


def run_game():
    game = Game(
        rules='Answer "yes" if the number is even, otherwise answer "no".',
        generate_round=generate_round,
        game_rounds=3,
    )
    run(game)
