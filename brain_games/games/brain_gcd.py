import random

from brain_games.games.engine import Game, run

MIN_NUMBER = 1
MAX_NUMBER = 100


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


def generate_round() -> tuple[str, str]:
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{first_number} {second_number}'

    answer = gcd(first_number, second_number)
    return question, str(answer)


def run_game():
    game = Game(
        rules='Find the greatest common divisor of given numbers.',
        generate_round=generate_round,
        game_rounds=3,
    )
    run(game)
