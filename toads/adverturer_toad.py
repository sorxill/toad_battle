"""
Toad Adventurer class
Has special abilities as like as doubling the damage done together with a chance of 2%
"""
import random

from toads.base_toad import Toad


class ToadAdventurer(Toad):
    """
    Toad class for adventurer
    """

    def __init__(self, name):
        super().__init__(name)

    def get_attack(self) -> int:
        """
        Get the damage has a chance to be doubled with chance 2%

        :return: int
        """
        damage = random.randint(1, self.damage)
        getting_damage = random.choices([2*damage, damage], cum_weights=(2, 98), k=1)[0]
        return getting_damage

    def given_damage(self, damage: int) -> None:
        """
        Base given damage for toad
        Change the instance health
        :param damage: int

        :return: None
        """
        receive_damage = self.armored_damage(damage)
        self.health -= receive_damage

    def armored_damage(self, damage: int) -> int:
        """
        Base armored damage with instance armor params
        :param damage: int

        :return: int
        """
        ignore_damage = random.randint(0, self.armor)
        receive_damage = damage - ignore_damage
        if receive_damage <= 0:
            return 0
        else:
            return receive_damage
