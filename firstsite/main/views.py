from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the main index.")


def about(request):
    return HttpResponse("Page for us")


def help(request):
    return HttpResponse("Help page")
    