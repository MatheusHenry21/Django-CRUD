from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Hello world
def teste(request: HttpRequest):
    return HttpResponse('Hello world!')
