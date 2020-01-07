# -*- coding: utf-8 -*-
"""Pokepy calls module.

This module contains all pokeapi calls that are need in the
whole project. Separating this in a single module, we abstract
the client initiation and can have some more complex API requests
with some logic included.

"""

import pokepy
from random import randrange
from typing import List, Union
from pokemon import Pokemon

client = pokepy.V2Client(cache='in_disk')

def get_move(name: str) -> pokepy.resources_v2.MoveResource:
    return client.get_move(name)

def get_pokemon(identifier: Union[str, int]) -> pokepy.resources_v2.MoveResource:
    return client.get_pokemon(identifier)


def get_random_pokemon(pokemons: int, level: int) -> Pokemon:
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

def get_all_abilities(pokemons: int) -> List[str]:
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