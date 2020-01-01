from dataclasses import dataclass
from pokemon import Pokemon
from poketypes import Stats

@dataclass
class BattleState:
    pokemon: Pokemon
    hp: int
    stats: Stats

    def calc_damage(self, damage):
        defense = self.pokemon.stats.defense
        self.hp = self.hp - damage + defense