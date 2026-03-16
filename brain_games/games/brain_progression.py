import random
from itertools import count, islice

from brain_games.games.engine import Game, run

MIN_NUMBER = 1
MAX_NUMBER = 100
MIN_STEP = 1
MAX_STEP = 10
MIN_LENGHT = 5
MAX_LENGHT = 10


def get_sequence() -> list[str]:
    start_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    step = random.randint(MIN_STEP, MAX_STEP)
    length = random.randint(MIN_LENGHT, MAX_LENGHT)

    progression = count(start_number, step)
    return [str(number) for number in islice(progression, length)]


def generate_round() -> tuple[str, str]:
    sequence = get_sequence()

    hidden_index = random.randint(0, len(sequence) - 1)
    answer = sequence[hidden_index]

    sequence[hidden_index] = '..'
    question = ' '.join(sequence)
    return question, answer


def run_game():
    game = Game(
        rules='What number is missing in the progression?',
        generate_round=generate_round,
        game_rounds=3,
    )
    run(game)
