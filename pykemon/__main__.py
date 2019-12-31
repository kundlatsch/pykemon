import pokepy
from pokemon import Pokemon

def get_abilities(client, pokemons):
    abilities = set()
    for i in range(pokemons):
        pokemon = client.get_pokemon(i+1)
        for raw_ability in pokemon.abilities:
            abilities.add(raw_ability.ability.name)
    return abilities

def main():
    client = pokepy.V2Client(cache='in_disk')
    
    # abilities = get_abilities(client, 150)
    # print(abilities)

    # print(dir(client.get_pokemon(4)))
    charizard = Pokemon(client.get_pokemon('charizard'), 50)

if __name__ == "__main__":
    main()