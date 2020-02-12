from django.db import models

# Create your models here.
from endereco.models import Endereco


class DocumentosPessoais(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=15)
    email = models.CharField(max_length=150)
    dataNascimento = models.CharField(max_length=150)
    telefone = models.CharField(max_length=150, null=True, blank=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    fotoRecibo = models.ImageField(upload_to='fotoRecibo', null=True, blank=True)


    def __str__(self):
        return self.nome


class RetornoRecibo():
    def __init__(self, nome, logradouro, numero, cep, cpfCnpj, complemento):
        self.nome = nome
        self.logradouro = logradouro
        self.numero = numero
        self.cep = cep
        self.cpfCnpj = cpfCnpj
        self.complemento = complemento