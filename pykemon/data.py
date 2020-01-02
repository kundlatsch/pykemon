"""Type effectiveness table

This dict has all the 18 types in it's keys
and 3-tuples as values. The 3-tuples elements
are sets, the first one have the types that the
key is strong against, the second are the ones
it is weak and the third are the types that the
key type is ineffective.
Source: https://bulbapedia.bulbagarden.net/wiki/Type
"""

EFFECTIVENESS = {

    'normal': (
        [],
        ['steel', 'rock'],
        ['ghost']
    ),

    'fight': (
        ['normal', 'rock', 'steel', 'ice', 'dark'],
        ['flying', 'poison', 'bug', 'psychic', 'fairy'],
        ['ghost']
    ),
    
    'flying': (
        ['fight', 'bug', 'grass'],
        ['rock', 'steel', 'electric'],
        []
    ),

    'poison': (
        ['grass', 'fairy'],
        ['poison', 'ground', 'rock', 'ghost'],
        ['steel']
    ),

    'ground': (
        ['poison', 'rock', 'steel', 'fire', 'electric'],
        ['bug', 'grass'],
        ['flying']
    ),

    'rock': (
        ['flying', 'bug', 'steel', 'fire', 'ice'],
        ['fight', 'ground', 'steel'],
        []
    ),

    'bug': (
        ['grass', 'psychic', 'dark'],
        ['fight', 'flying', 'poison', 'ghost', 'steel', 'fire', 'fairy'],
        []
    ),

    'ghost': (
        ['ghost', 'psychic'],
        ['dark'],
        ['normal']
    ),

    'steel': (
        ['rock', 'ice', 'fairy'],
        ['steel', 'fire', 'water', 'electric'],
        []
    ),

    'fire': (
        ['bug', 'steel', 'grass', 'ice'],
        ['rock', 'fire', 'water', 'dragon'],
        []
    ),

    'water': (
        ['ground', 'rock', 'fire'],
        ['water', 'grass', 'dragon'],
        []
    ),

    'grass': (
        ['ground', 'rock', 'water'],
        ['flying', 'poison', 'bug', 'steel', 'fire', 'grass', 'dragon'],
        []
    ),

    'electric': (
        ['flying', 'water'],
        ['grass', 'electric', 'dragon'],
        ['ground']
    ),

    'psychic': (
        ['fight', 'poison'],
        ['steel', 'psychic'],
        ['dark']
    ),

    'ice': (
        ['flying', 'ground', 'grass', 'dragon'],
        ['steel', 'fire', 'water', 'ice'],
        []
    ),

    'dragon': (
        ['dragon'],
        ['steel'],
        ['fairy']
    ),

    'dark': (
        ['ghost', 'psychic'],
        ['dark', 'fairy'],
        []
    ),

    'fairy': (
        ['fight', 'dragon', 'dark'],
        ['poison', 'steel', 'fire'],
        []
    )

}