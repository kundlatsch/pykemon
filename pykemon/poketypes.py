# -*- coding: utf-8 -*-
"""Project's types module.

This module contains the types used into different parts of the whole
project. The types are NamedTuples ore dataclass structures.

"""


from pokepy import resources_v2 as pokepy
from dataclasses import dataclass
from typing import NamedTuple

class VersionedMove(NamedTuple):
    move: pokepy.MoveResource
    version: pokepy.PokemonMoveSubResource

@dataclass
class Stats():
    speed: int
    special_defense: int
    special_attack: int
    defense: int
    attack: int
    hp: int
