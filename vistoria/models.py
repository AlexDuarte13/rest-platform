from django.db import models

from automovel.models import Automovel
from documentosPessoais.models import DocumentosPessoais

# Create your models here.

class Vistoria(models.Model):

    nome = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    documentosPessoais = models.OneToOneField(DocumentosPessoais, on_delete=models.CASCADE, null=True, blank=True)
    automovel = models.ForeignKey(Automovel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome