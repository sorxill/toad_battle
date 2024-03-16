"""
Craftsman toad class
Has special abilities as like as absorbing incoming damage by 30% with a 20% chance
"""
import random

from toads.base_toad import Toad


class ToadCraftsman(Toad):
    """
    Toad class for craftsman
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
        Given damage has a chance to be lower 30%
        Change the instance health
        :param damage: int

        :return: None
        """
        receive_damage = self.armored_damage(damage)
        out_damage = random.choices([0.7*receive_damage, receive_damage], cum_weights=(20, 80), k=1)[0]
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
