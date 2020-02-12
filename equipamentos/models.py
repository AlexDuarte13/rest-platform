from django.db import models

# Create your models here.
class Equipamento(models.Model):

    nome = models.TextField(null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome