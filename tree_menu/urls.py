from django.urls import path
from .views import index, menu_detail

urlpatterns = [
    path("menu/", index),
    path("menu/<slug:menu_item_slug>/", menu_detail, name="menu_detail"),
]
