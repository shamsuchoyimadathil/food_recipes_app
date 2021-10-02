from django import forms
from . import models

class RecipesForm(forms.ModelForm):
    class Meta:
        model = models.Recipes 
        fields = "__all__"
        labels = {
            'food_name':('Recipe name:'),
            'description':('Short description of your food:'),
            'image':('Add a photo of your Recipe:'),
            'preparation_time':('Preparation time (min):'),
            'ingredients':('Ingredients of your recipe:'),
            'preparation':('How to cook:'),
            'category':('give a category:'),
            'native_food_of':('which type of this food ?'),
            'cuisine_type':('Choose a type:'),


        }
        
    def __init__(self,*args, **kwargs):
        super(RecipesForm,self).__init__(*args, **kwargs)
        self.fields['food_name'].widget.attrs=({'placeholder':'recipe name'})
        self.fields['description'].widget.attrs=({'placeholder':'give small description for this Recipe'})
        self.fields['image'].widget.attrs=({'label':'Add a photo of your Recipe:'})
        self.fields['preparation_time'].widget.attrs=({'placeholder':'preparation time in minutes'})
        self.fields['ingredients'].widget.attrs=({'placeholder':'seaparete eachone with comma(,) and start eachone with dashes(-)'})
        self.fields['preparation'].widget.attrs=({'placeholder':'write about how to make this recipe'})
        self.fields['category'].widget.attrs=({'placeholder':'eg:sweet,spicy,peppery etc...'})
        self.fields['native_food_of'].widget.attrs=({'placeholder':'eg:indian,italian,arabian etc...'})
        
