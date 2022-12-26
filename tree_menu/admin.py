from django.contrib import admin
from .models import MenuItem, Menu


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "parent", "menu")
    list_display_links = ("id", "slug", "parent", "menu")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Menu)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug")
    list_display_links = ("id", "slug")
    prepopulated_fields = {"slug": ("title",)}
