from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string

db_data=[
    {"id":1, "good":"Fork", "describe":"I get this fork from my grandma Elizaphet|| queen of Britan", "price":"9000$", "is_published":True},
    {"id":2, "good":"RX 8900 XTX 50 GB", "describe":"I'm come from future and wanna sold my ancient GPU(2028 year) with 50 gb video ram 1024bit DDR7.5ulitmate", "price":"2700$", "is_published":True},
    {"id":3, "good":"Misha", "describe":"good guy Django developer, however our habits strong differ + he drink all mounth stock coffee in brief term, therefore i'm wanna sold him for yours goals", "price":"400$/month + car + house in front of sea + 1m$ + bycicle", "is_published":True},
]
def index(request):
    context = {
        "title" : "rozetka.com",
        "mainmenu" : [
        {"title":"about site","url":"about"},
        {"title":"add goods","url":"addgood"},
        {"title":"futher information","url":"finfo"},
        {"title":"log in","url":"log"},
        ],
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
        "title":"about us"
    }
    return render(request,"goodscat/finfo.html" ,context=context)

def log(request):
    return HttpResponse("this func coming soon")
def nfound(request, exception):
    return HttpResponseNotFound("not found page")