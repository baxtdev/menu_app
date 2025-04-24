from django import template
from menu.models import Menu
from menu.utils import build_tree, get_active_branch

register = template.Library()

@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    path = request.path
    menu = Menu.objects.prefetch_related('items__children').get(name=menu_name)
    all_items = list(menu.items.all())

    tree = build_tree(all_items)
    active_branch = get_active_branch(path, all_items)
    return {'menu_tree': tree, 'active_branch': active_branch, 'request': request}