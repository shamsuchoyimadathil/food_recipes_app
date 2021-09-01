from django.db.models import fields
import django_filters
from django_filters.filters import CharFilter 
from . import models

class RecipesFilters(django_filters.FilterSet):
    name = CharFilter(field_name="food_name",lookup_expr="icontains", label='')
    class Meta:
        model = models.Recipes
        fields = ['name']
        
    def __init__(self,*args, **kwargs):
        super(RecipesFilters,self).__init__(*args, **kwargs)
        self.filters['name'].field.widget.attrs=({'placeholder':'search', 'class':'form-control mr-sm-2'})