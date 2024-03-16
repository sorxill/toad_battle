"""
Metaclass with abc methods for all toads
"""
from abc import ABC, abstractmethod

from data.base_data_toad import ToadData


class Toad(ABC, ToadData):
    """
    Metaclass Toad
    Data from ToadData
    Necessary fields:
    name: str
    """
    @abstractmethod
    def get_attack(self) -> int:
        """
        abstractmethod for getting the attack
        return attack value with special params

        :return: int
        """
        ...

    @abstractmethod
    def given_damage(self, damage: int) -> None:
        """
        abstractmethod for given damage
        this method change the health params for current toad
        :param damage: int

        :return: None
        """
        ...

    @abstractmethod
    def armored_damage(self, damage: int) -> int:
        """
        abstractmethod for armored damaged
        this method is called from given damage to armor input damage
        return received damage
        :param damage: int

        :return: int
        """
        ...
