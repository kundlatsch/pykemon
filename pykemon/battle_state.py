from dataclasses import dataclass
from pokemon import Pokemon
from poketypes import Stats

@dataclass
class BattleState:
    pokemon: Pokemon
    stats: Stats
