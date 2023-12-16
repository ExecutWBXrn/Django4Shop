from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string

def index(request):
    return render(request, "goodscat/index.html")

def about(request):
    return render(request, "goodscat/about.html")
def nfound(request, exception):
    return HttpResponseNotFound("not found page")