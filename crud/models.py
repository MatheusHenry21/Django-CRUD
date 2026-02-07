from django.db import models

# Model de Agenda de Cll
class ContatoModel(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name