from django.urls import path,register_converter
from .views import *
from .converter import *
register_converter(Sluglim5symbConverter,"Lim5Slug")
urlpatterns = [
    path('', index),
]