import pokepy
from random import randrange

import client
from pokemon import Pokemon

def get_all_abilities(pokemons):
    """ Get all abilities from a given number of pokémon
    
    Args:
        pokemons: upper search limit (numbered by Pokédex).
    Returns:
        A set of all abilities from all pokémon in the given limit.
    """
    abilities = set()
    for i in range(pokemons):
        pokemon = client.get_pokemon(i+1)
        for raw_ability in pokemon.abilities:
            abilities.add(raw_ability.ability.name)
    return abilities

def get_random_pokemon(pokemons, level):
    """ Return a random pokémon inside the given limit.
    
    Args:
        pokemons: upper random selection limit (numbered by Pokédex).
        level: level of the random pokémon generated.
    Returns:
        A random Pokémon object.
    """
    
    pokemon_id = randrange(pokemons + 1)
    pokemon = client.get_pokemon(pokemon_id)

    return Pokemon(pokemon, level)



def main():
    
    # abilities = get_abilities(client, 150)
    # print(abilities)

    # print(dir(client.get_pokemon(4)))
    p = get_random_pokemon(150, 50)
    print(p.name)
    p.print_moves()

if __name__ == "__main__":
    main()