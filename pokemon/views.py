"""
Go to views.py, and create a detail view for your pokemons.
Call the function get_pokemon.
The function will receive a request, a pokemon_id, and return an HttpResponse.
The function should use the pokemon_id received from the parameters to fetch the Pokemon from the database.
The HttpResponse should contain a multi-line string, that is also an f-string, which displays the details of our pokemon.
"""

from django.http import HttpResponse
from rest_framework.generics import ListAPIView , RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Pokemon
from .serializers import ListPokemonSerializer , DetailPokemonSerializer, UpdatePokemonSerializer, AddPokemonSerializer, EditPokemonSerializer
def get_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    return HttpResponse(pokemon.get_html())



"""API for Retreviel API"""
class PokeObjAPIView(RetrieveAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = DetailPokemonSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'pokemon_id'

"""API for Update API"""
class PokeObjUpdateAPIView(UpdateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = UpdatePokemonSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'pokemon_id'

"""API for delete API"""
class PokeObjDeleteAPIView(DestroyAPIView):
    queryset = Pokemon.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'pokemon_id'

"""API for Add API"""
class PokeObjCreateAPIView(CreateAPIView):
    # queryset = Pokemon.objects.all()
    serializer_class = AddPokemonSerializer
    # lookup_field = 'id'
    # lookup_url_kwarg = 'pokemon_id'

"""CRUD API"""
class PokeRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = EditPokemonSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'pokemon_id'
    




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


class PokeListApiView(ListAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = ListPokemonSerializer

