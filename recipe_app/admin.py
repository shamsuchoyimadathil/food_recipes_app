from django.contrib import admin
from . import models

# Register your models here.

class RecipesAdmin(admin.ModelAdmin):
    list_display = ('food_name','category',"cuisine_type")
    list_filter = ("category","cuisine_type","native_food_of")

admin.site.register(models.Recipes,RecipesAdmin)