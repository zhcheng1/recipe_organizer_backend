from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Recipe(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(blank=True, null=True, default="This is a default description", help_text="This is a quick description of your recipe")
    directions = models.TextField(default="This is a default direction", help_text="How to make the recipe")
    ingredients = models.ManyToManyField(Ingredient)


    def __str__(self):
        return self.name + ": " + self.description





