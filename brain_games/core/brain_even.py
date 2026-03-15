import random

import prompt

MAX_ATTEMPTS = 3
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 1000


def show_rules() -> None:
    print('Answer "yes" if the number is even, otherwise answer "no".')


def process_game() -> bool:
    for _ in range(MAX_ATTEMPTS):
        number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
        print(f'Question: {number}')

        user_answer = prompt.string('Your answer: ')

        correct_answer = 'yes' if number % 2 == 0 else 'no'

        if correct_answer == user_answer:
            print("Correct!")
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            return False

    return True


def show_result(user_name: str, game_result: bool) -> None:
    if game_result:
        print(f"Congratulations, {user_name}!")
    else:
        print(f"Let's try again, {user_name}!")
