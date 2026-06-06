from django.db import models


class Banco(models.Model):
    nomec = models.CharField(max_length=100, null=False)
    idadec = models.IntegerField(null=False)
    raca = models.CharField(max_length=50, null=True)
    doenca = models.CharField(max_length=50, null=True)
    imagem = models.URLField(max_length=500, null=True, blank=True)
    