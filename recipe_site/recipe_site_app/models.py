from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title_category= models.CharField(max_length=200,  unique=True)

    def __str__(self):
        return f'{self.title}'


class Recipes(models.Model):
    category = models.ManyToManyField(Category,
                                      verbose_name="Категория")
    title_recipe = models.CharField(max_length=200, unique=True,
                             verbose_name="Название рецепта")
    description = models.TextField(default="",
                                   verbose_name="Краткое описание")
    ingredients = models.TextField(default="",
                                         verbose_name="Ингридиенты")
    cooking_steps = models.TextField(default="",
                                     verbose_name="Процесс приготовления")
    cooking_time = models.IntegerField(default=0,
                                       verbose_name="Время готовки")
    image = models.ImageField(null=True, blank=True, upload_to="recipes_img/", verbose_name='Фотография')
    views = models.IntegerField(default=0,
                                verbose_name="Количество просмотров")
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name="Автор рецепта")
    date_of_publications = models.DateTimeField(auto_now_add=True,
                                            verbose_name="Время публиуации")
    date_of_editing = models.DateTimeField(auto_now=True,
                                          verbose_name="Отредактировано")

   
    def __str__(self):
        return self.title