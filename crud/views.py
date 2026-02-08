
from django.shortcuts import render, redirect
from django.http import HttpRequest
from . import forms
from . import models

#HOME com POST
def home_orm(request: HttpRequest):
    return render(request, 'crud/html/index.html')

def contato_post(request: HttpRequest): 
    if request.method == 'POST':
        formulario = forms.ContatoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('crud:home')
    
    context = {
        'info': forms.ContatoForm()
    }
    return render(request, 'crud/html/adicionar.html', context)

def contato_get(request):
    context = {
        'info': models.ContatoModel.objects.all()
    }

    return render(request, 'crud/html/listar.html', context)

def contato_patch(request: HttpRequest):
    return render(request, 'crud/html/atualizar.html')