# -*- coding: utf-8 -*-
"""Pokémon math module, used in battles

This module contains functions that are used by
the battle class. They are in a separeted module
to prevent them from being contained directly in
the 'Battle' class and allowing them to be used
separately by the library user. 
"""

from errors import InvalidAttackType
from random import randrange


def calc_damage(atk_pokemon, def_pokemon, move):
    """ Damage calculation function, based on Gen VII specifications.
        
        Args:
            atk_pokemon: Pokemon that will attack.
            def_pokemon: Pokemon that will be attacked.
            atk_type: Attack type - physical (1) or special (2). String or int can be used.
        Returns:
            Total amount of damage given to def_pokemon.
    """

    atk_type = move.damage_class.name

    if atk_type == 'physical' or atk_type == 1:
        attack = atk_pokemon.stats.attack
        defense = def_pokemon.stats.defense

    elif atk_type == 'special' or atk_type == 2:
        attack = atk_pokemon.stats.special_attack
        defense = def_pokemon.stats.special_defense

    else:
        raise InvalidAttackType("The selected move is a "
                                "status one, not an attack.")

    # The damage calculation follows the formula from
    # https://bulbapedia.bulbagarden.net/wiki/Damage

    # In generation 1, a critical hit doubles the level (not using here)
    level_damage = ((2 * atk_pokemon.level) / 5) + 2
    power = move.power
    attack_fraction = attack/defense

    base_damage = ((level_damage * power * attack_fraction) / 50) + 2
    
    # Modifier variables
    
    # Simplified target to 1, once we only have 1v1 fights at the moment
    target = 1
    # Simplified weather to 1, once we do not have weather implemented yet
    weather = 1
    # Badge not applied (this feature only appeared in gen 2)
    critical = calc_critical(atk_pokemon.stats.speed, move)
    
    if critical:
        # add critical logic
        pass
    
    # TODO: add all modifier variables
    
    modifier = target * weather
        
    final_damage = base_damage * modifier

    return final_damage

def calc_critical(speed, move):
    """Calculate if an attack was a critical hit or not.

    Args:
        speed: The speed of the attacking pokémon.
        move: The attack used.
    Returns:
        True if the attack was a critical hit, false otherwise.
    """

    # Critical chance calculated based on:
    # https://bulbapedia.bulbagarden.net/wiki/Critical_hit

    threshold = speed / 2
    random_number = randrange(255)

    if random_number < threshold:
        return True
    else:
        return False

