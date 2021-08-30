from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from . import models
from . import forms

# Create your views here.

def main(request):
    context = {}

    recipes = models.Recipes.objects.all()
    context['recipes'] = recipes

    return render(request,"recipe/main.html",context)
    

def add_recipe(request):

    context = {}

    add_recipe_form = forms.RecipesForm(request.POST,request.FILES)

    if add_recipe_form.is_valid():
        cleaned_data = add_recipe_form.cleaned_data
        data = models.Recipes(food_name = cleaned_data['food_name'] , description = cleaned_data['description'],
                              image = cleaned_data['image'],preparation_time= cleaned_data['preparation_time'],
                              ingredients = cleaned_data['ingredients'],preparation=cleaned_data['preparation'],
                              category=cleaned_data['category'], native_food_of = cleaned_data['native_food_of'],
                              cuisine_type=cleaned_data['cuisine_type'])

        data.save()
        return HttpResponseRedirect("/") 
    else:
        add_recipe_form = forms.RecipesForm 

    context['form'] = add_recipe_form

    return render(request,"recipe/add_recipe.html",context)
        # food_name = models.Recipes(cleaned_data['food_name'])
        # description = models.Recipes(cleaned_data['description'])
        # image = models.Recipes(cleaned_data['image'])
        # preparation_time = models.Recipes(cleaned_data['preparation_time'])
        # ingredients = models.Recipes(cleaned_data['ingredients'])
        # preparation = models.Recipes(cleaned_data['preparation'])
        # category = models.Recipes(cleaned_data['category'])
        # native_food_of = models.Recipes(cleaned_data['native_food_of'])
        # cuisine_type = models.Recipes(cleaned_data['cuisine_type'])

