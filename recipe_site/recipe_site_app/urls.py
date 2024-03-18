from django.urls import path
from . import views

app_name = 'recipe_site_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
]