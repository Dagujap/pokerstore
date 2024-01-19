import requests
import json

def pokemon_list() -> dict:
    try:
        res = requests.get("https://pokeapi.co/api/v2/pokemon")
        res = json.loads(res.content)
    except Exception as ex:
        print(ex) #TODO:You need to manage this exception

    return res


def get_pokemon(url: str) -> dict:
    res = requests.get(url)
    res = json.loads(res.content)

    pokemon = {
        "name": res["forms"][0]["name"],
        "image": res["sprites"]["back_default"]
    }

    return pokemon


def get_pokemon_images(url: str) -> dict:
    res = requests.get(url)
    res = json.loads(res.content)

    images = res["sprites"]

    return images