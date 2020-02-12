from django.db import models

# Create your models here.
class DocumentosPessoaisImoveis(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=15)
    dataRegistro = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    dataNascimento = models.CharField(max_length=150, null=True, blank=True)
    telefone = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.nome + ' - ' + self.cpf + ' - ' + str(self.dataRegistro)