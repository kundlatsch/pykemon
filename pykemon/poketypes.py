import pokepy
from dataclasses import dataclass
from typing import NamedTuple



class VersionedMove(NamedTuple):
    move: pokepy.resources_v2.MoveResource
    version: pokepy.resources_v2.PokemonMoveSubResource

@dataclass
class Stats():
    speed: int
    special_defense: int
    special_attack: int
    defense: int
    attack: int
    hp: int
