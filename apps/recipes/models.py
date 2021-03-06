
from django.db import models
from PIL import Image


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True, help_text="This is a quick description of your recipe")
    directions = models.TextField(help_text="How to make the recipe")
    ingredients = models.TextField(max_length=400)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    recipe = models.ForeignKey(Recipe)
    title = models.CharField (max_length=30)
    reviews = models.TextField(help_text="User review here.")
    star = models.PositiveIntegerField(blank=True, null=True)
    username = models.CharField(max_length=20)

    def __str__(self):
        return "%s's review" %(self.recipe)


