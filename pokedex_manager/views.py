from django.shortcuts import render
from pokemon_manager.services import (
    get_pokemon_list_with_pagination,
    get_pokemon_images,
)

# Create your views here.
def foo(request):
    pokemons = get_pokemon_list_with_pagination()
    pokemon_list = []

    for pokemon in pokemons["results"]:
        images = get_pokemon_images(pokemon["url"])
        
        pokemon_list.append({
            "name": pokemon["name"],
            "image": images["front_default"],
        })

    return render(
        request=request,
        template_name="pages/list_view_pokemon.html", 
        context={"pokemons":pokemon_list}
    )