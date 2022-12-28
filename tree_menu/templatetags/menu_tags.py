from django import template
from tree_menu.models import MenuItem

register = template.Library()


def find_item_parent(item, result, menu_item):
    new_result = []
    finded = False
    for result_item in result:
        if item.parent == result_item["item"] and not finded:
            print(menu_item)
            result_item["children"].append(
                {"item": item, "children": [], "open": menu_item == item.slug}
            )
            result_item["open"] = menu_item == item.slug
            new_result.append(result_item)
            finded = False
        elif not finded:
            result_item["children"] = find_item_parent(
                item, result_item["children"], menu_item
            )
            if result_item["children"] and result_item["children"][0]["open"]:
                result_item["open"] = True
            new_result.append(result_item)
            finded = False
        else:
            new_result.append(result_item)
    return new_result


@register.inclusion_tag("tree_menu/menu.html", name="draw_menu")
def show_menu(menu_slug, menu_item=None):
    items = MenuItem.objects.filter(menu__slug=menu_slug)
    result = []
    for item in items:
        if item.parent == None:
            result.append(
                {"item": item, "children": [], "open": item.slug == menu_item}
            )
        else:
            result = find_item_parent(item, result, menu_item)
    context = {"items": result}
    print(context)
    return context
