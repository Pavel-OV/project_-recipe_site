# Generated by Django 5.0.2 on 2024-03-19 19:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_category', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_recipe', models.CharField(max_length=200, unique=True, verbose_name='Название рецепта')),
                ('description', models.TextField(default='', verbose_name='Краткое описание')),
                ('ingredients', models.TextField(default='', verbose_name='Ингридиенты')),
                ('cooking_steps', models.TextField(default='', verbose_name='Процесс приготовления')),
                ('cooking_time', models.IntegerField(default=0, verbose_name='Время готовки')),
                ('image', models.ImageField(blank=True, null=True, upload_to='recipes_img/', verbose_name='Фотография')),
                ('views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('date_of_publications', models.DateTimeField(auto_now_add=True, verbose_name='Время публиуации')),
                ('date_of_editing', models.DateTimeField(auto_now=True, verbose_name='Публикация отредактирована')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор рецепта')),
                ('category', models.ManyToManyField(to='recipe_site_app.category', verbose_name='Категория')),
            ],
        ),
    ]
