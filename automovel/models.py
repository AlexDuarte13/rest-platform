from django.db import models

# Create your models here.
from equipamentos.models import Equipamento


class Automovel(models.Model):

    placa = models.CharField(max_length=150, null=True, blank=True)
    ufPlaca = models.CharField(max_length=15, null=True, blank=True)
    chassi = models.CharField(max_length=150, null=True, blank=True)
    renavam = models.CharField(max_length=150, null=True, blank=True)
    marcaModelo = models.CharField(max_length=150, null=True, blank=True)
    anoDoVeiculo = models.CharField(max_length=4, null=True, blank=True)
    # equipamentos = models.ManyToManyField(Equipamento, blank=True)
    km = models.CharField(max_length=15, null=True, blank=True)
    cor = models.CharField(max_length=100, null=True, blank=True)
    combustivel = models.CharField(max_length=100, null=True, blank=True)
    tipoVeiculo = models.CharField(max_length=100, null=True, blank=True)
    capacidadePassageiros = models.CharField(max_length=3, null=True, blank=True)
    fabricante = models.CharField(max_length=100, null=True, blank=True)
    fotoCNH = models.ImageField(upload_to='fotoCNH', null=True, blank=True)
    fotoCRLV = models.ImageField(upload_to='fotoCRLV', null=True, blank=True)
    fotoDianteiraDireita = models.ImageField(upload_to='fotoDianteiraDireita', null=True, blank=True)
    fotoDianteiraEsquerda = models.ImageField(upload_to='fotoDianteiraEsquerda', null=True, blank=True)
    fotoTraseiraDireita = models.ImageField(upload_to='fotoTraseiraDireita', null=True, blank=True)
    fotoTraseiraEsquerda = models.ImageField(upload_to='fotoTraseiraEsquerda', null=True, blank=True)

    def __str__(self):
        return self.placa

class RetornoImagem(models.Model):
    porcentagem = models.TextField
    descricao = models.TextField

    def __init__(self, porcentagem, descricao):
        self.porcentagem = porcentagem
        self.descricao = descricao

class RetornoCRLV():
    def __init__(self, placa, uf, chassi, renavam, marcaModelo, anoVeiculo):
        self.placa = placa
        self.uf = uf
        self.chassi = chassi
        self.renavam = renavam
        self.marcaModelo = marcaModelo
        self.anoVeiculo = anoVeiculo
