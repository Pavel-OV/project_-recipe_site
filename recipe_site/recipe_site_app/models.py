from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, \
    MinLengthValidator


app_label = 'recipe_site_app'


class RecipeCategories(models.Model):
    title = models.CharField(max_length=200,  unique=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = "Категории рецептов"
        verbose_name = "категории рецептов"


class Recipes(models.Model):
    title = models.CharField(validators=[MinLengthValidator(3)],
                              max_length=200, verbose_name='Название рецепта')
    description = models.TextField(
        max_length=4000, verbose_name='Описание рецепта', default="")
    cooking_steps = models.TextField(
        verbose_name='Последовательность приготовления', default="")
    ingredients = models.TextField(
        blank=True, null=True, verbose_name='Ингредиенты')
    category = models.ManyToManyField(
        RecipeCategories, verbose_name="Категория")
    cooking_time_in_minutes = models.IntegerField(
        validators=[MinValueValidator(1)], verbose_name='Время приготовления')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')
    image = models.ImageField(
        upload_to='photos_cooked_recipes/', blank=True, null=True, verbose_name='Изображение блюда')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор рецепта')
    publicated_date = models.DateField(
        auto_now_add=True, verbose_name='Дата создания')
    chaged_date = models.DateField(auto_now=True, verbose_name='Дата редактирования')

    def __str__(self):
        return f'Recipes {self.title}  '

    class Meta:
        verbose_name_plural = "Рецепты"
        verbose_name = "рецепт"


class CommentsOnRecipe(models.Model):
    # author = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Автор рецепта')
    recipe = models.ForeignKey(
        Recipes, on_delete=models.CASCADE, verbose_name=' Рецепт')
    comment = models.TextField(max_length=3000, verbose_name='Комментарий')
    publicated_date = models.DateField(
        auto_now_add=True, verbose_name='Дата создания')
    chaged_date = models.DateField(auto_now=True, verbose_name='Автор')

    def __str__(self):
        return f'{self.comment}'

    class Meta:
        verbose_name_plural = "Комментарии к рецептам"
        verbose_name = "комментарии к рецептам"
