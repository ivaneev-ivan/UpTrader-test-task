from django import template
from tree_menu.models import MenuItem

register = template.Library()


@register.inclusion_tag("tree_menu/menu.html", name="draw_menu")
def show_menu(menu_slug):
    items = MenuItem.objects.filter(menu__slug=menu_slug, parent=None)
    return {"items": items}
