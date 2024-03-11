from django.db import models
from users.models import Users
from django.core.validators import MinValueValidator, \
                                   MinLengthValidator


app_label = 'recipe_site_app'


class Recipes(models.Model):
    title = models.CharField(validators=[MinLengthValidator(3)], max_length=50, verbose_name='Название рецепта')
    description = models.TextField(max_length=1000, verbose_name='Описание рецепта')
    cooking_steps = models.TextField(verbose_name='Последовательность приготовления')
    products = models.TextField(blank=True, null=True, verbose_name='Ингредиенты')
    cooking_time_in_minutes = models.IntegerField(validators=[MinValueValidator(1)],verbose_name='Время приготовления')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')
    image = models.ImageField(upload_to='photos_cooked_recipes/', blank=True, null=True, verbose_name='Картинка')
  

    def __str__(self):
        return f'Recipes( ' \
               f'title: {self.title}, ' \
               f' )'

    class Meta:
        verbose_name_plural = "Рецепты"
        verbose_name = "рецепт"


class RecipeCategories(models.Model):
    title = models.CharField(validators=[MinLengthValidator(3)], max_length=100, unique=True, verbose_name='Категория')
    recipes = models.ManyToManyField(Recipes)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = "Категории рецептов"
        verbose_name = "категории рецептов"


class CommentsOnRecipe(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, verbose_name=' Рецепт')
    comment = models.TextField(max_length=3000, verbose_name='Комментарий')
    publicated_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    chaged_date = models.DateField(auto_now=True, verbose_name='Автор')

    def __str__(self):
        return f'{self.comment}'

    class Meta:
        verbose_name_plural = "Комментарии к рецептам"
        verbose_name = "комментарии к рецептам"