import requests


def pokemon_list() -> dict:
    #TODO:¨return pagination
    res = requests.get("https://pokeapi.co/api/v2/pokemon")
    res = res.json()

    return res

def get_pokemon(url: str) -> dict:
    res = requests.get(url)
    res = res.json()

    pokemon = {
        "name": res["forms"][0]["name"],
        "image": res["sprites"]["back_default"]
    }

def get_pokemon_images(url: str) -> dict:
    res = requests.get(url)
    res = res.json()

    images = res["sprites"]

    return images
