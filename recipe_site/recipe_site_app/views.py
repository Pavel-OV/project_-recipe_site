from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import NewRecipe
from .models import Recipes


def index(request):
    return render(request, "recipe_site_app/index.html")


def new_recipe(request):
    form = NewRecipe(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            if request.FILES:
                image = form.cleaned_data['image']
                fs = FileSystemStorage()
                fs.save(image.name, image)
            else:
                image = None

            title_recipe = form.cleaned_data['title_recipe']
            author = request.user
            description = form.cleaned_data['description']
            ingredients = form.cleaned_data['ingredients']

            category = form.cleaned_data['category']
            cooking_time = form.cleaned_data['cooking_time']
            cooking_steps = form.cleaned_data['cooking_steps']
            recipe = Recipes.objects.create(title_recipe=title_recipe, image=image,
                                            author=author, description=description,
                                            cooking_time=cooking_time, cooking_steps=cooking_steps,
                                            ingredients=ingredients)

            recipe.category.add(*category)
            message = 'Рецепт добавлен'

            return render(request, 'recipe_site_app/new_recipe.html', {'form': form, 'message': message})
        else:
            return render(request, 'recipe_site_app/new_recipe.html', {'form': form,
                                                                       'message': 'Форма недействительна'})

    else:
        form = NewRecipe()
        message = 'Заполните форму для рецепта'
        return render(request, 'recipe_site_app/new_recipe.html', {'form': form, 'message': message})


def all_recipes(request):
    recipes = Recipes.objects.all()
    return render(request, 'recipe_site_app/all_recipes.html', {'recipes': recipes})

