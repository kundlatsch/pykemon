import pokepy

client = pokepy.V2Client(cache='in_disk')

def get_move(name):
    return client.get_move(name)

def get_pokemon(identifier):
    return client.get_pokemon(identifier)