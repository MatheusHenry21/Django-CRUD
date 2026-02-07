
from django.shortcuts import render
from django.http import HttpRequest
from . import forms

# Hello world
def home_orm(request: HttpRequest):

    context = {
        'info': forms.ContatoForm
    }

    return render(request, 'crud/html/index.html', context)
