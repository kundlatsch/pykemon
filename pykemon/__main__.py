import pokepy

import client
from pokemon import Pokemon
from battle_state import BattleState
from pokemath import calc_damage

def main():
    
    p1 = Pokemon(client.get_pokemon(3), 50)
    # p1 = BattleState(p, p.stats)

    p2 = Pokemon(client.get_pokemon(6), 50)
    for move in p2.moves:
        print(move.move.name)
    calc_damage(p1, p2, p1.moves[0].move)


if __name__ == "__main__":
    main()