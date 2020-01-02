# -*- coding: utf-8 -*-
"""Pokémon math module, used in battles

This module contains functions that are used by
the battle class. They are in a separeted module
to prevent them from being contained directly in
the 'Battle' class and allowing them to be used
separately by the library user. 
"""

from errors import InvalidAttackType
from random import randrange, randint
from data import EFFECTIVENESS


def calc_damage(atk_pokemon, def_pokemon, move):
    """Damage calculation function, based on Gen VII specifications.
        
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
    
    # Random: a value between 0.85 and 100
    random = randint(85, 100) / 100
    
    # STAB: same-type attack bonus
    # If the pokémon attack's has the same type of the
    # pokémon itself, the attack has 50% more damage
    
    stab = 1.0
    for pokemon_type in atk_pokemon.types:
        if pokemon_type.name == move.type.name:

            if atk_pokemon.ability == 'adaptability':
                stab = 2.0
            else:
                stab = 1.5



    critical = calc_critical(atk_pokemon.stats.speed, move)
    if critical:
        # add critical logic
        pass
    
    # TODO: add all modifier variables

    # Type effectiveness multiplier
    effectiveness = get_type_effectiveness(move.type.name, def_pokemon.types)
    
    modifier = target * weather * random * stab * effectiveness
        
    final_damage = base_damage * modifier 

    return int(final_damage)

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

def get_type_effectiveness(atk_type, def_types):
    """Get the effectiveness multiplier based on the attack type and the defender types.
    
    Args:
        atk_type: The attack type name.
        def_types: A list with the defending pokémon types.
    Returns:
        The effectiveness multiplier.
    """

    strong, weak, ineffective = EFFECTIVENESS[atk_type]

    # Effective sum, used to compute effectiveness in case
    # of the defender pokémon having more than one type.
    eff_sum = 0

    for def_type in def_types:
        
        if def_type.name in ineffective:
            return 0

        elif def_type.name in strong:
            eff_sum = eff_sum + 2

        elif def_type.name in weak:
            eff_sum = eff_sum - 2

    
    # Attack weak against 1 defending type
    if eff_sum == -2:
        return 1/2
    
    # Attack weak against 2 defending types
    if eff_sum == -4:
        return 1/4
    
    # Attack neutral against defending pokémon
    if eff_sum == 0:
        return 1
    
    # Attack strong against one or both defeding types
    return eff_sum
    