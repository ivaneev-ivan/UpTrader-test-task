# Generated by Django 4.1.4 on 2022-12-26 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Menu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="Название меню"),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=100, unique=True, verbose_name="slug меню"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MenuItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="Название элемента"),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=100, unique=True, verbose_name="slug элемента"
                    ),
                ),
                (
                    "menu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tree_menu.menu",
                        verbose_name="Меню элемента",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tree_menu.menuitem",
                        verbose_name="Родитель элемента",
                    ),
                ),
            ],
            options={
                "verbose_name": "элемент меню",
                "verbose_name_plural": "элементы меню",
            },
        ),
    ]