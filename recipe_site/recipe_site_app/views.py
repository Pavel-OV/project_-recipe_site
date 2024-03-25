from django.shortcuts import get_object_or_404, render
from django.core.files.storage import FileSystemStorage
from .forms import NewRecipe, RecipeSearchForm
from .models import Recipes, Category
from django.db.models import Q


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


def all_user_recipes(request, author_id):
    if author_id:
        recipes = Recipes.objects.filter(
            author=author_id).order_by('-date_of_publications')
        return render(request, 'recipe_site_app/all_user_recipes.html', {'recipes': recipes})


def user_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipes, pk=recipe_id)
    recipe.views += 1
    recipe.save()

    title_category = Category.objects.filter().values_list('title_category', flat=True)

    ingredients = Recipes.objects.filter(
        id=recipe_id).values_list("ingredients", flat=True)

    return render(request, 'recipe_site_app/user_recipe.html',
                  {'recipe': recipe, 'title_category': title_category, 'ingredients': ingredients})


def update_recipe(request, recipe_id):
    recipe = Recipes.objects.filter(pk=recipe_id).first()
    form = NewRecipe(request.POST, request.FILES, instance=recipe)
    if request.method == 'POST':
        if form.is_valid():
            if request.FILES:
                image = form.cleaned_data['image']
                fs = FileSystemStorage()
                fs.save(image.name, image)
            else:
                image = None
            recipe.image = image
            category = form.cleaned_data['category']
            recipe.title_recipe = form.cleaned_data['title_recipe']
            recipe.description = form.cleaned_data['description']
            recipe.ingredients = form.cleaned_data['ingredients']
            recipe.cooking_time = form.cleaned_data['cooking_time']
            recipe.cooking_steps = form.cleaned_data['cooking_steps']
            recipe.save()
            recipe.category.add(*category)
            message = 'рецепт обновлен !'
            return render(request, 'recipe_site_app/update_recipe.html', {'form': form, 'message': message})

    else:
        recipe = Recipes.objects.get(pk=recipe_id)
        form = NewRecipe(instance=recipe)
        message = 'внесите нужные исправления в рецепт'
        return render(request, 'recipe_site_app/update_recipe.html', {'form': form, 'message': message})


def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipes, pk=recipe_id)
    recipe.delete()
    message = 'Рецепт удален'
    return render(request, 'recipe_site_app/user_recipe.html', {'message': message})


def search(request):
    categories = Category.objects.all()
    ingredients = list(Recipes.objects.all())
    form = RecipeSearchForm(request.GET)
    message = None
    if request.method == 'POST':
        category_id = request.POST.get('category')
        ingredient_id = request.POST.get('ingredients')
        if category_id:
            cat_name = get_object_or_404(Category, pk=category_id)
            recipes = Recipes.objects.filter(category=cat_name)
            search_ref = "категории"
        elif ingredient_id:
            cat_name = get_object_or_404(Recipes, pk=ingredient_id)
            recipes = Recipes.objects.filter(ingredients=cat_name)
            search_ref = "ингридиенту"
        else:
            return render(request, 'recipe_site_app/search.html',
                          {'form': form, 'categories': categories, 'ingredients': ingredients})
        if not recipes:
            message = "ничего не найдено"
        return render(request, 'recipe_site_app/search.html',
                      {'recipes': recipes, 'cat_name': cat_name, 'search_ref': search_ref, 'categories': categories,
                       'ingredients': ingredients, 'message': message, 'form': form, })

    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            recipes = Recipes.objects.filter(
                Q(title_recipe__iregex=query) |
                Q(description__iregex=query) |
                Q(cooking_steps__iregex=query))
        else:
            recipes = None
        if not recipes:
            message = "ничего не найдено"
        cat_name = query
        search_ref = ''
        return render(request, 'recipe_site_app/search.html',
                      {'recipes': recipes, 'cat_name': cat_name, 'search_ref': search_ref, 'categories': categories,
                       'ingredients': ingredients, 'form': form, 'message': message})

    return render(request, 'recipe_site_app/search.html',
                  {'form': form, 'categories': categories, 'ingredients': ingredients, 'message': message})


def search_category(request, cat):
    message = None
    categories = Category.objects.all()    
    cat_id = get_object_or_404(Category, title_category=cat)
    recipes = Recipes.objects.filter(category=cat_id.pk)
    form = RecipeSearchForm(request.GET)
    if not recipes:
        message = "ничего не найдено"
    search_ref = "категории"
    return render(request, 'recipes/search.html', {'recipes': recipes, 'cat_name': cat,
                                                   'search_ref': search_ref, 'categories': categories,
                                                   'message': message, 'form': form, })

