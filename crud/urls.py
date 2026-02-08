from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    path('', views.home_orm, name='home'),
    path('adicionar/', views.contato_post, name='adicionar'),
    path('listar/', views.contato_get, name='listar'),
    path('atualizar/', views.contato_patch, name='atualizar')
]