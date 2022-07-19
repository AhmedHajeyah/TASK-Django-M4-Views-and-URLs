"""
Go to views.py, and create a detail view for your pokemons.
Call the function get_pokemon.
The function will receive a request, a pokemon_id, and return an HttpResponse.
The function should use the pokemon_id received from the parameters to fetch the Pokemon from the database.
The HttpResponse should contain a multi-line string, that is also an f-string, which displays the details of our pokemon.
"""

from django.http import HttpResponse

from .models import Pokemon

def get_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    return HttpResponse(pokemon.get_html())