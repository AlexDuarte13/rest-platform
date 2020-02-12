from django.db import models

# Create your models here.

class Endereco(models.Model):
    cep = models.CharField(max_length=150)
    logradouro = models.CharField(max_length=150, null=True, blank=True)
    numero = models.CharField(max_length=100)
    complemento = models.CharField(max_length=70)
    bairro = models.CharField(max_length=70)
    cidade = models.CharField(max_length=70)
    uf = models.CharField(max_length=70)

    def __str__(self):
        return self.logradouro