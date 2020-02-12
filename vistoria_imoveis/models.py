from django.db import models

# Create your models here.
from documentos_pessoais_imoveis.models import DocumentosPessoaisImoveis
from endereco.models import Endereco
from imovel.models import Imovel


class VistoriaImoveis(models.Model):

    nome = models.CharField(max_length=100)
    dataRegistro = models.DateTimeField(auto_now_add=True)
    documentosPessoaisImoveis = models.OneToOneField(DocumentosPessoaisImoveis, on_delete=models.CASCADE, null=True, blank=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    imovel = models.OneToOneField(Imovel, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.nome + ' - ' + self.documentosPessoaisImoveis.cpf + ' - ' + str(self.dataRegistro)