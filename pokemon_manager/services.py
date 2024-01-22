# public functions to share with anothers internal applications
from pokemon_manager.api.pokeapi import (
    pokemon_list,
    get_pokemon_images,
)

def get_pokemon_list_with_pagination():
    return pokemon_list()

def get_pokemon_images():
    return get_pokemon_images()