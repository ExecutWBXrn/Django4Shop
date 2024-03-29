from django.urls import path,register_converter
from .views import *
from .converter import *

register_converter(Sluglim5symbConverter,"Lim5Slug")

urlpatterns = [
    path('', index, name="home"),
    path('aboutsite/', about, name="about"),
    path('addgoods/', addgood, name="addgood"),
    path('finfo/', finfo, name="finfo"),
    path('log/', log, name="log"),
    path('categories/', categories, name="cat"),
    path('categories/<slug:cat_slug>', dis_cat, name="dcat"),
    path('goodinfo/<slug:good_slug>', furtherinfo, name="goodinfo"),
    path('tag/', tag, name="tag_path"),
    path('tag/<slug:tag_slug>/', tag_tag_slug, name="tag_tag_slug_path"),
]