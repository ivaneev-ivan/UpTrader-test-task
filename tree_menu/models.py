from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название элемента")
    slug = models.SlugField(max_length=100, verbose_name="slug элемента", unique=True)
    parent = models.ForeignKey(
        "MenuItem",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Родитель элемента",
    )
    menu = models.ForeignKey(
        "Menu", on_delete=models.CASCADE, verbose_name="Меню элемента"
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "элемент меню"
        verbose_name_plural = "элементы меню"


class Menu(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название меню")
    slug = models.SlugField(max_length=100, verbose_name="slug меню", unique=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "меню"
        verbose_name_plural = "меню"
