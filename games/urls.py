"""games URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))





Go to urls.py and create a path for our pokemon detail view.
Import our get_pokemon view.
Add a path that is starts with pokemons/ and contains an id in its path.

"""
from django.contrib import admin
from django.urls import path
from pokemon.views import get_pokemon, get_pokemons, PokeListApiView, PokeObjAPIView, PokeObjUpdateAPIView, PokeObjDeleteAPIView, PokeObjCreateAPIView, PokeRUDAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pokemon/<int:pokemon_id>", get_pokemon),
    path("pokemons/", get_pokemons),
    
    #API Endpoints
    path("pokemonapi/", PokeListApiView.as_view()),
    path("poke/<int:pokemon_id>", PokeObjAPIView.as_view()),
    path("poke/update/<int:pokemon_id>", PokeObjUpdateAPIView.as_view()),
    path("poke/delete/<int:pokemon_id>", PokeObjDeleteAPIView.as_view()),
    path("poke/add/", PokeObjCreateAPIView.as_view()),

    #CRUD API
    path("poke/rud/<int:pokemon_id>", PokeRUDAPIView.as_view()),

]
