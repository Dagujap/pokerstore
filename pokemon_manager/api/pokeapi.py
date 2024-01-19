import requests

def pokemon_list():
    pokemon = requests.get("https://pokeapi.co/api/v2/pokemon")
    return pokemon

    