from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from . import models
from . import forms
from . import filters
# Create your views here.

def main(request):
    context = {}
    recipes = models.Recipes.objects.all()
    filter = filters.RecipesFilters(request.GET, queryset=recipes)
    recipes = filter.qs

  

    if recipes is None or len(recipes)==0:
        context["no_result"] = True
        

    context['recipes'] = recipes
    context['filter'] = filter 


    # context['no_results'] = recipes.__len__ = 0

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



def detail(request,id):
    context = {}
    detail_view = models.Recipes.objects.get(pk=id)
    context['detail'] = detail_view 

    return render(request,"recipe/detail.html",context) 


def favourites(request):

    
    if request.method == "GET":
        favourite_recipes = request.session.get('favourite_recipes')
        context = {} 

        if favourite_recipes is None or len(favourite_recipes)==0:
            context['recipes'] = []
            context['has_recipes'] = False 

        else:
            recipes = models.Recipes.objects.filter(id__in=favourite_recipes)
            context['recipes'] = recipes 
            context['has_recipes'] = True 

        return render (request,"recipe/favourite.html",context)

    if request.method == "POST":
        favourite_recipes = request.session.get("favourite_recipes")
        if favourite_recipes is None:
            favourite_recipes = []

        favourite_id = int(request.POST["favourite_id"])

        if 'add' in request.POST:
            if favourite_id not in favourite_recipes:
                favourite_recipes.append(favourite_id)

        elif 'remove' in request.POST:
            if favourite_id in favourite_recipes:
                favourite_recipes.remove(favourite_id)
            
        request.session['favourite_recipes'] = favourite_recipes 

        return HttpResponseRedirect('/')
 

    return render (request,"recipe/favourite.html")