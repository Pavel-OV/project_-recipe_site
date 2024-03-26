from django.contrib import admin
from .models import Recipes, Category
from .models import *

admin.site.register(Recipes)
admin.site.register(Category)