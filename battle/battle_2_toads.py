"""
Battle system two toads
The toad class need to be changed manually
Uncomment ToadAdventurer import to use this class
"""
from toads.assassin_toad import ToadAssassin
from toads.base_toad import Toad
from toads.craftsman_toad import ToadCraftsman
# from toads.adventurer_toad import ToadAdventurer


def battle(toad1: Toad, toad2: Toad) -> Toad | str:
    """
    Main function to battle 2 toads.
    Need two toads which has main type "Toad"
    :param toad1: Toad

    :param toad2: Toad

    :return: Toad | str
    """
    while toad1.health > 0 and toad2.health > 0:
        attack_toad_1: int = toad1.get_attack()
        attack_toad_2: int = toad2.get_attack()
        toad1.given_damage(attack_toad_2)
        toad2.given_damage(attack_toad_1)

    if toad1.health > 0:
        return toad1

    if toad2.health > 0:
        return toad2

    else:
        return "ничья"


def get_battle(battles: int, name1: str, name2: str) -> str:
    """
    Main function to get battles.
    Necessary params is count of battles and 2 names for toads

    :param battles: int

    :param name1: str

    :param name2: str

    :return: str
    """
    win_1 = 0
    win_2 = 0
    for i in range(battles):
        ass = ToadAssassin(name=name1)
        craft = ToadCraftsman(name=name2)
        result = battle(ass, craft)
        if result == ass:
            win_1 += 1
        if result == craft:
            win_2 += 1

    return f"%{name1}% %{win_1}% побед\n%{name2}% %{win_2}% побед"
