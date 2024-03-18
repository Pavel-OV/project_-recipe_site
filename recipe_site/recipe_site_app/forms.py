from django import forms
from django.db import DatabaseError, OperationalError
from django.forms import ModelForm, TextInput, Textarea
from .models import RecipeCategories, Recipes

CATEGORY_CHOICES =[('Первое блюдо', "Первое блюдо"), ('Второе блюдо','Второе блюдо'),
('Напитки', 'Напитки'),("Салаты", "Салаты"),("Выпечка", "Выпечка"), ('Консервация','Консервация' ), ("Другое", 'Другое')]



# class RecipesForm(forms.Form):
#     title  = \
#         forms.CharField(
#             required=True,
#             min_length=3,
#             max_length=200,
#             label='Название рецепта',
#             widget=forms.TextInput(
#                 attrs={'class': 'form_add_one_recipes',
#                        'placeholder': 'Название рецепта (обязательное поле)'}),
#         )
#     description = forms.CharField(
#             required=True,
#             min_length=3,
#             max_length=4000,
#             label='Краткое описание рецепта',
#             widget=forms.Textarea(
#                 attrs={'class': 'form_add_one_recipes__description',
#                        'placeholder': 'Введите краткое не более 1000 '
#                        'символов описание рецепта '
#                        '(обязательное поле)'}),
#         )
#     cooking_steps = forms.CharField(
#             required=True,
#             label='Содержание рецепта',
#             widget=forms.Textarea(
#                 attrs={'class': 'form_add_one_recipes__cooking_steps',
#                        'placeholder': 'Введите сам рецепт (обязательное поле)'}),
#         )
#     ingredients = forms.CharField(
#             required=False,
#             label='Необходимые продукты',
#             widget=forms.Textarea(
#                 attrs={'class': 'form_add_one_recipes__description',
#                        'placeholder': 'Введите необходимые для приготовлдения '
#                        'рецепта продукты (не обязательное поле)'}),
#         )

#     category = forms.MultipleChoiceField(
#         required=True,
#         label='Категория (обязательное поле):',
#         widget=forms.SelectMultiple(
#             attrs={'class': 'form_add_one_recipes__multiple_choice_field'}),
#         category=RecipeCategoriesForms('category')
#     )
#     cooking_time_in_minutes = forms.IntegerField(
#             required=True,
#             label='Время готовки минут (обязательное поле)',
#             widget=forms.NumberInput(
#                 attrs={'class': 'form_add_one_recipes__cooking_time_in_minutes', 'min': 1})
#         )
#     image =  forms.ImageField(
#             required=False,
#             label='Фотография блюда (не обязательное поле)',
#             widget=forms.FileInput(
#                 attrs={'class': 'form_add_one_recipes__image'})
#     )

   
    


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['title_recipe', 'description', 'cooking_steps', 'title_categories', 'cooking_time_in_minutes',
                'ingredients', 'image']
        # widgets = {
            
        #     'title_categories': forms.Select( choices=CATEGORY_CHOICES)
        # }
        widgets = {
            'title': TextInput(attrs={'size': 77}),
            'description': Textarea(attrs={'cols': 80, 'rows': 5}),
            'cooking_steps': Textarea(attrs={'cols': 80, 'rows': 7})}
        _
    

# class RecipeCategoriesForms(forms.Form):
#     title = forms.ChoiceField(choices=[('First_course', "Первое блюдо"), ('Second_course','Второе блюдо'),
#                         ('Drinks', 'Напитки'),("Salads", "Салаты"),
#                         ("Bakery_products", "Выпечка"),("Porridge", "Каши"), ("Other", 'Другое')])
    

class RecipeCategoriesForms(forms.ModelForm):
    class  Meta:
        model = RecipeCategories
        fields = ['title_categories']
        widgets = {
            
            'title_categories': forms.Select( choices=CATEGORY_CHOICES)
        }

        
class RecipeCategoriesFormsV2(forms.ModelForm):
    class  Meta:
        model = RecipeCategories
        fields = ['title_categories']
        widgets = {
            
            'title_categories': forms.Select( choices=CATEGORY_CHOICES)
        }
