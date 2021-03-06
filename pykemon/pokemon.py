import pokepy
from pokepy import resources_v2 as pokepy

import client
from random import sample
from poketypes import VersionedMove, Stats


class Pokemon:

    def __init__(self, pokemon: pokepy.PokemonResource, level: int):
        self.pokeAPI_data = pokemon
        self.id = pokemon.id
        self.name = pokemon.name
        self.level = level
        self.moves = self.select_moves()
        self.stats = self.get_stats()
        self.types = self.get_types()
        self.ability = self.get_ability()
        

    def get_all_moves(self, generation: str):
        """Return the pokémon's all leveling-up learned moves from the given genertion.
        
        Args:
            generation: The name of the generation from which moves are selected (see PokeAPI for more information). 
        Returns:
            A list of all the pokémon leveling-up learned moves.
        """

        pokemon = self.pokeAPI_data
        all_moves = []
        for move in pokemon.moves:
            for version in move.version_group_details:
                
                learn_method = version.move_learn_method.name
                game_version = version.version_group.name

                move_name = move.move.name

                if learn_method == 'level-up' and game_version == generation:
                    move_resource = client.get_move(move_name)
                    all_moves.append(VersionedMove(move_resource, version))
        
        # Sort moves by level using lambda function
        all_moves.sort(key = lambda move: move.version.level_learned_at, reverse=True)
        
        return all_moves
    
    def select_moves(self):
        """Select pokemon's four moves, based on pokémon current level
        
        Returns:
            A list of four VersionedMoves
        """
        
        all_moves = self.get_all_moves("ultra-sun-ultra-moon")
        selected_moves = []

        for move in all_moves:
            if move.version.level_learned_at <= self.level:
                selected_moves.append(move)
            if len(selected_moves) == 4:
                return selected_moves
        
        return selected_moves

    def get_stats(self):
        """Get pokémon stats, returning a Stats named tuple"""

        pokemon = self.pokeAPI_data
        stat_list = []
        
        for stat in pokemon.stats:
            stat_list.append(stat.base_stat)
        
        # Using * to unpack the list
        stats = Stats(*stat_list)

        return stats

    def print_moves(self):
        """Print the pokémon's four moves"""

        for versioned_move in self.moves:
            print(versioned_move.move.name)
        
    def get_types(self):
        """Return a list with the pokémon types (one or two types)"""
        pokemon = self.pokeAPI_data
        types = []
        for pokemon_type in pokemon.types:
            types.append(pokemon_type.type)
        
        return types
    
    def get_ability(self):
        """Get one random ability from pokémon's possible abilities"""
        pokemon = self.pokeAPI_data
        abilities = set()
        
        for ability in pokemon.abilities:
            abilities.add(ability.ability.name)
        
        [ability] = sample(abilities, 1)

        return ability