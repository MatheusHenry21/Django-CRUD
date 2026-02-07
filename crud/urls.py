from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    path('', views.home_orm, name='home'),
    path('adicionar/', views.contato_post, name='adicionar')
]