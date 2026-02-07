
from django.shortcuts import render
from django.http import HttpRequest



# Hello world
def teste(request: HttpRequest):
    return render(request, 'crud/index.html')
