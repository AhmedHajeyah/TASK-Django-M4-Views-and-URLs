from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
 


class Pokemon(models.Model):
    class PokemonType(models.TextChoices):
        WATER = "WA"
        GRASS = "GR"
        GHOST = "GH"
        STEEL = "ST"
        FAIRY = "FA"

    name = models.CharField(max_length=30)
    type = models.CharField(max_length=2, choices=PokemonType.choices)
    hp = models.PositiveIntegerField(
        validators=[MinValueValidator(50), MaxValueValidator(350)]
    )
    active = models.BooleanField(default=True)

    # Localizations
    name_fr = models.CharField(max_length=30, default="", blank=True)
    name_jp = models.CharField(max_length=30, default="", blank=True)
    name_ar = models.CharField(max_length=30, default="", blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_html(self):
        return f"<h1>{self.name}</h1>\n<p>{self.type}</p>\n<p>{self.hp}</p>"