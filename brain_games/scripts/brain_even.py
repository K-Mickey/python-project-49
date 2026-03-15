from brain_games.cli import welcome_user
from brain_games.core.brain_even import process_game, show_result, show_rules


def main():
    user_name = welcome_user()
    show_rules()
    game_result = process_game()
    show_result(user_name=user_name, game_result=game_result)


if __name__ == '__main__':
    main()
