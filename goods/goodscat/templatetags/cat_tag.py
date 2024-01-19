from django import template
import goodscat.views as views

register = template.Library()

@register.simple_tag(name="cat")
def categories():
    return views.cat_db

@register.simple_tag()
def mainmenu():
    menu = [
        {"title": "home", "url": "home"},
        {"title": "about site", "url": "about"},
        {"title": "add goods", "url": "addgood"},
        {"title": "futher information", "url": "finfo"},
        {"title": "log in", "url": "log"},
        {"title": "categories", "url": "cat"},
        {"title": "tags", "url": "tag_path"},
    ]
    return menu