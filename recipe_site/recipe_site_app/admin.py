from django.contrib import admin
from .models import Recipes, Category


@admin.register(Recipes)
class RecipesModelAdmin(admin.ModelAdmin):
    list_display = ['title_recipe', 'author','cooking_time', 'views','date_of_publications']
    readonly_fields = ['date_of_publications',]
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title_recipe',"description",],
            },
        ),
        (
            
            'Полная информация о рецепте',
            
            {
                
                'classes': ['collapse'],
                'description': 'Информация о рецепте',
                'fields': ["ingredients",'cooking_steps','cooking_time',],
            },
        ),
    ]

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title_category',]
