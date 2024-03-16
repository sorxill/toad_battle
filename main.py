"""
Main entry point for game
"""
from battle.battle_2_toads import get_battle


def main():
    """
    Main function to game

    :return: None
    """
    ans = get_battle(battles=100, name1="assassin", name2="craftsman")
    print(ans)


if __name__ == "__main__":
    main()
