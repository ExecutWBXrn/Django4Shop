from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from .models import Goods
db_data=Goods.objects.all()

cat_db = [
    {"id":1, "title":"sport"},
    {"id":2, "title":"computers"},
    {"id":3, "title":"shoes"},
    {"id":4, "title":"flats"},
    {"id":5, "title":"something else"},
]
def index(request):
    context = {
        "title" : "rozetka.com",
        "DB_data" : db_data,
    }
    return render(request, "goodscat/index.html", context=context)

def about(request):
    context = {
        "title" : "foxtrot.com",
    }
    return render(request, "goodscat/about.html", context=context)

def addgood(request):
    return HttpResponse("this func not ready yet")

def finfo(request):
    context={
        "title":"about us",
    }
    return render(request,"goodscat/finfo.html" ,context=context)

def log(request):
    return HttpResponse("this func coming soon")

def categories(request):
    context = {
        "title":"categories"
    }
    return render(request, "goodscat/categories.html", context=context)

def furtherinfo(request, good_slug):
    w=get_object_or_404(Goods, slug=good_slug)
    context = {
        "title":w.good,
        "good_slug":good_slug,
        "db":db_data,
    }
    return render(request, "goodscat/goodinfo.html", context=context)
def nfound(request, exception):
    return HttpResponseNotFound("not found page")