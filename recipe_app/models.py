from django.db import models

# Create your models here.

CUISINE_TYPE = (
    ('veg','Veg'),
    ('vegan','Vegan'),
    ('eggetarian','Eggetarian'),
    ('non veg','Non Veg')
)

class Recipes(models.Model):
    food_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to = "food_images")
    preparation_time = models.PositiveIntegerField()
    ingredients = models.CharField(max_length=100)
    preparation = models.TextField()
    category = models.CharField(max_length=20)
    native_food_of = models.CharField(blank=True,max_length=20)
    cuisine_type = models.CharField(max_length=20,choices=CUISINE_TYPE)

    def __str__(self):
        return self.food_name