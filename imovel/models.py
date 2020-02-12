from django.db import models

# Create your models here.
class Imovel(models.Model):

    dataRegistro = models.DateTimeField(auto_now_add=True)
    quantidade_quartos = models.IntegerField(null=True, blank=True)
    quantidade_salas = models.IntegerField(null=True, blank=True)
    quantidade_cozinha = models.IntegerField(null=True, blank=True)
    quantidade_banheiro = models.IntegerField(null=True, blank=True)
    quantidade_quintal = models.IntegerField(null=True, blank=True)
    fotoSala = models.ImageField(upload_to='fotoSala', null=True, blank=True)
    fotoQuarto = models.ImageField(upload_to='fotoQuarto', null=True, blank=True)
    fotoBanheiro = models.ImageField(upload_to='fotoBanheiro', null=True, blank=True)
    fotoCozinha = models.ImageField(upload_to='fotoCozinha', null=True, blank=True)


    def __str__(self):
        return str(self.dataRegistro)