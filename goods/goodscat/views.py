from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string

def index(request):
    context = {
        "title" : "rozetka.com",
    }
    return render(request, "goodscat/index.html", context=context)

def about(request):
    context = {
        "title" : "foxtrot.com",
    }
    return render(request, "goodscat/about.html", context=context)
def nfound(request, exception):
    return HttpResponseNotFound("not found page")