"""
Toad Assassin class
Has special abilities as like as a complete dodge of the damage received with a chance of 5%
"""
import random

from .base_toad import Toad


class ToadAssassin(Toad):
    """
    Toad class for assassin
    """

    def __init__(self, name):
        super().__init__(name)

    def get_attack(self) -> int:
        """
        Base attack for toad

        :return: int
        """
        random_damage_range = random.randint(1, self.damage)
        return random_damage_range

    def given_damage(self, damage: int) -> None:
        """
        Given damage has a chance to be 0 with 5% chance
        Change the instance health
        :param damage: int

        :return: None
        """
        receive_damage = self.armored_damage(damage)
        out_damage = random.choices([0, receive_damage], cum_weights=(5, 95), k=1)[0]
        self.health -= out_damage

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
