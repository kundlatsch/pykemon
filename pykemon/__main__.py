import pokepy

import client
from pokemon import Pokemon
from pokemath import calc_damage

def main():
    
    p1 = Pokemon(client.get_pokemon(3), 50)
    # p1 = BattleState(p, p.stats)

    p2 = Pokemon(client.get_pokemon(6), 50)
    print(f'{p1.name} vs {p2.name}')
    print(f'{p1.moves[0].move.name}')
    dmg = calc_damage(p1, p2, p1.moves[0].move)
    print(dmg)

if __name__ == "__main__":
    main()