from django import forms
from django.forms import TextInput, Textarea

from .models import Recipes
from django.utils.translation import gettext as _


class NewRecipe(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['title_recipe', 'description', 'cooking_steps', 'category', 'cooking_time',
                  'ingredients', 'image']
        widgets = {
            'title_recipe': TextInput(attrs={'size': 60}),
            'description': Textarea(attrs={'cols': 60, 'rows': 5}),
            'cooking_steps': Textarea(attrs={'cols': 60, 'rows': 7})}

class RecipeSearchForm(forms.Form):
    query = forms.CharField(label='Поиск по тексту', max_length=200, empty_value="", required=False,
                            widget=forms.TextInput(attrs={"style": "width: 400px;"}))