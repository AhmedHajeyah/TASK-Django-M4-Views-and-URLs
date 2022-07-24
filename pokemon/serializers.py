
"""
creating serializers.py
"""

from rest_framework import serializers
from .models import Pokemon

class ListPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'

class DetailPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('name', 'type', 'hp')

class UpdatePokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('name', 'type', 'hp')
        # read_only_fields = ('name', 'type', 'hp')

class AddPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'
        # read_only_fields = ('name', 'type', 'hp')

class EditPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'
        # read_only_fields = ('name', 'type', 'hp')