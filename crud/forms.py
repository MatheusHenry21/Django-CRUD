
from django.forms import ModelForm
from . import models

class ContatoForm(ModelForm):
    class Meta:
        model = models.ContatoModel
        fields = [
            'name',
            'phone'
        ]