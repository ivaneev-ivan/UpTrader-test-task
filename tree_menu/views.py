from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import MenuItem


def index(request):
    return render(request, "tree_menu/index.html", {"menu_item": None})


def menu_detail(request, menu_item_slug):
    menu_item = get_object_or_404(MenuItem, slug=menu_item_slug)
    return render(request, "tree_menu/index.html", {"menu_item": menu_item.slug})
