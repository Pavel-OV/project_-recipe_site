from django.urls import path
from . import views

app_name = 'recipe_site_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('new_recipe/', views.new_recipe, name='new_recipe'),
    path('all_recipes/', views.all_recipes, name='all_recipes'),
    path('all_user_recipes/<int:author_id>/', views.all_user_recipes, name='all_user_recipes'),
    path('update_recipe/<int:recipe_id>/', views.update_recipe, name='update_recipe'),
    path('user_recipe/<int:recipe_id>', views.user_recipe, name='user_recipe'),
    
]
