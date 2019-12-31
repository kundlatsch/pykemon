import pokepy
from pokemon import Pokemon

def get_abilities(client, pokemons):
    """ Get all abilities from a given number of pokémon
    
    Args:
        client: pokepy client to get the pokémon.
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

def get_random_pokemon(pokemons):
    """ Return a random pokémon from the given limit.
    
    Args:
        pokemons: upper random selection limit (numbered by Pokédex).
    Returns:
        A random Pokémon object.
    """

    pass



def main():
    client = pokepy.V2Client(cache='in_disk')
    
    # abilities = get_abilities(client, 150)
    # print(abilities)

    # print(dir(client.get_pokemon(4)))
    charizard = Pokemon(client.get_pokemon('charizard'), 50)

if __name__ == "__main__":
    main()