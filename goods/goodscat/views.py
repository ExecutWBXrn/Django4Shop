from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return HttpResponse("goods")

def nfound(request, exception):
    return HttpResponseNotFound("not found page")