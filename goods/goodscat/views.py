from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from .models import Goods, Category, TagPost
db_data=Goods.objects.all()
cat_db=Category.objects.all()
tag_db=TagPost.objects.all()
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

def dis_cat(request, cat_slug):
    w=get_object_or_404(Category, slug=cat_slug)
    context = {
        "title":w.name,
        "cat_slug":cat_slug,
        "DB_data":db_data,
    }
    return render(request, "goodscat/display_cat.html", context=context)

def furtherinfo(request, good_slug):
    w=get_object_or_404(Goods, slug=good_slug)
    context = {
        "title":w.good,
        "good_slug":good_slug,
        "db":db_data,
        "post":w,
    }
    return render(request, "goodscat/goodinfo.html", context=context)

def tag(request):
    context={
        "title":"tags",
        "tag_db":tag_db,
    }
    return render(request, "goodscat/tag.html", context=context)
def tag_tag_slug(request, tag_slug):
    w=get_object_or_404(TagPost, slug=tag_slug)
    good_db=w.tags.filter(is_published=Goods.STATUS.PUBLISHED)
    context={
        "title":w.name,
        "tag_slug":tag_slug,
        "good_db":good_db,
    }
    return render(request, "goodscat/tag_tag_slug.html", context=context)
def nfound(request, exception):
    return HttpResponseNotFound("not found page")