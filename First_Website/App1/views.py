from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "App1/index.html")

def A(request):
    return HttpResponse("Hello, A!")

def B(request):
    return HttpResponse("Hello, B!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")