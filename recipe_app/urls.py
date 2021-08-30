from django.conf.urls import url
from django.urls import path 

from . import views

urlpatterns = [
    path("",views.main, name="main-page"),
    path("addrecipe",views.add_recipe,name="add-recipe"),
    path("detailpage/<int:id>",views.detail,name="detail-page")
]
