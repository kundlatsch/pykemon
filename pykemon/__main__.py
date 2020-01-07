import pokepy

import client
from pokemon import Pokemon
from pokemath import calc_damage
from battle import BattleState, Battle


def main():
    
    p1 = Pokemon(client.get_pokemon(3), 50)

    p2 = Pokemon(client.get_pokemon(6), 50)
    
    battle = Battle(p1, p2)
    battle.make_move(p1.moves[0])

if __name__ == "__main__":
    main()