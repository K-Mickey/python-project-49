import random

from brain_games.games.engine import Game, run

MIN_NUMBER = 1
MAX_NUMBER = 100
OPERATORS = ('+', '-', '*')


def generate_round() -> tuple[str, str]:
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(OPERATORS)
    question = f'{first_number} {operator} {second_number}'

    answer = str(eval(question))
    return question, answer


def run_game():
    game = Game(
        rules='What is the result of the expression?',
        generate_round=generate_round,
        game_rounds=3,
    )
    run(game)
