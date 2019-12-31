from typing import NamedTuple
import pokepy

class VersionedMove(NamedTuple):
    move: pokepy.resources_v2.PokemonMoveSubResource
    version: pokepy.resources_v2.PokemonMoveSubResource

class Stats(NamedTuple):
    speed: int
    special_defense: int
    special_attack: int
    defense: int
    attack: int
    hp: int


class Pokemon:

    def __init__(self, pokemon, level):
        self.pokeAPI_data = pokemon
        self.id = pokemon.id
        self.name = pokemon.name
        self.level = level
        self.moves = self.select_moves()
        self.stats = self.get_stats()
        

    def get_all_moves(self):
        """Return the pokémon's all leveling-up learned moves

        This function returns a list of all moves
        learned by leveling up. The list of moves is
        from the generation VIII (ultra sun and ultra moon),
        because it is the last game with all pokemons.
        """

        pokemon = self.pokeAPI_data
        all_moves = []
        for move in pokemon.moves:
            for version in move.version_group_details:
                
                learn_method = version.move_learn_method.name
                game_version = version.version_group.name

                if learn_method == 'level-up' and game_version == 'ultra-sun-ultra-moon':
                    all_moves.append(VersionedMove(move, version))
        
        # Sort moves by level using lambda function
        all_moves.sort(key = lambda move: move.version.level_learned_at, reverse=True)
        
        return all_moves
    
    def select_moves(self):
        """ Select pokemon's four moves

        In this implementation, the four most 
        recently learned movements are selected
        based on pokemon current level
        """
        
        all_moves = self.get_all_moves()
        selected_moves = []

        for move in all_moves:
            if move.version.level_learned_at <= self.level:
                selected_moves.append(move)
            if len(selected_moves) == 4:
                return selected_moves
        
        return selected_moves

    def get_stats(self):
        """ Get pokémon stats, returning a Stats named tuple """
        
        pokemon = self.pokeAPI_data
        stat_list = []
        
        for stat in pokemon.stats:
            stat_list.append(stat.base_stat)
        
        stats = Stats(*stat_list)

        return stats 