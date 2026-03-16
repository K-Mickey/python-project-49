import random

from brain_games.games.engine import Game, run

MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(number: int) -> bool:
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number < 2:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def generate_round() -> tuple[str, str]:
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_prime(number) else 'no'
    return str(number), answer


def run_game():
    game = Game(
        rules='Answer "yes" if given number is prime. Otherwise answer "no".',
        generate_round=generate_round,
        game_rounds=3,
    )
    run(game)
