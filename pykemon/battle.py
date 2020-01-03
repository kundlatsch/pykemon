from dataclasses import dataclass
from random import randint

from pokemon import Pokemon
from poketypes import Stats
from pokemath import calc_damage
from errors import InvalidMove

@dataclass
class BattleState:
    pokemon: Pokemon
    stats: Stats
    condition: str = None

class Battle:

    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = BattleState(pokemon1, pokemon1.stats)
        self.pokemon2 = BattleState(pokemon2, pokemon2.stats)
        # self.turn = randint(1, 2)
        self.turn = 1

    def get_active_pokemon(self):
        if self.turn == 1:
            return self.pokemon1
        else:
            return self.pokemon2
        
    def get_other_pokemon(self, active_pokemon):
        if active_pokemon == self.pokemon1:
            return self.pokemon2
        else:
            return self.pokemon1
    
    def make_move(self, versioned_move):
        atk_pokemon = self.get_active_pokemon()
        def_pokemon = self.get_other_pokemon(atk_pokemon)
        
        move = versioned_move.move

        # Get moves from pokémon's versioned moves
        moves =  []
        for v_move in atk_pokemon.pokemon.moves:
            moves.append(v_move.move)
        
        if move not in moves:
            raise InvalidMove(f"{atk_pokemon.pokemon.name}"
                              f" don't have the attack {move.move.name}")
        
        if move.damage_class.name != 'status':
            damage = calc_damage(atk_pokemon, def_pokemon, move)
            def_pokemon.stats.hp -= damage

        # TODO: Add move status logic!
