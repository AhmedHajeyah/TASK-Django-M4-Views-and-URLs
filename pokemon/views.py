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

"""
Go to views.py and create a list view for all our pokemons.
Call the function get_pokemons.
The function will receive a request, and return an HttpResponse.
The HttpResponse should contain a joined list of strings (separated by a new line), that displays the names of all our pokemons.
"""

def get_pokemons(request):
    pokemons = Pokemon.objects.all().values_list("name", flat=True)
    pokemons_list = "\n".join(f"<li>{pokemons}</li>" for pokemons in pokemons)
    return HttpResponse(f"<i>{pokemons_list}</i>")
