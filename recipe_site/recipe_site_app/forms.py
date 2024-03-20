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
            'title_recipe': TextInput(attrs={'size': 50}),
            'description': Textarea(attrs={'cols': 60, 'rows': 5}),
            'cooking_steps': Textarea(attrs={'cols': 60, 'rows': 7})}

