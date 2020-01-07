from random import randint

from pokemon import Pokemon
from poketypes import Stats, VersionedMove
from pokemath import calc_damage, accuracy_check, BattleState
from errors import InvalidMove

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
    
    def turn(self, p1_action, p2_action):
        
        

        if isinstance(p1_action, Pokemon):
            # change pokemon logic
            pass
        
        if isinstance(p2_action, Pokemon):
            # change pokemon logic
            pass
        
        if isinstance(p1_action, VersionedMove):
            pass
        
    
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
        
        move_cfg = (atk_pokemon, def_pokemon, move)

        if move.damage_class.name != 'status':
            if accuracy_check(*move_cfg):
                damage = calc_damage(*move_cfg)
                def_pokemon.stats.hp -= damage
        


        # TODO: Add move status logic!
