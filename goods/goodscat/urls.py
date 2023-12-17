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
]