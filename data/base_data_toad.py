"""
Dataclass to base toad
"""
from dataclasses import dataclass


@dataclass
class ToadData:
    """
    This is a data class.
    All toads need to have this fields.
    The name must be implemented by initialization
    """
    name: str
    health: int = 150
    damage: int = 10
    armor: int = 8
