from django.db import models
from django.urls import reverse


class UF(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.sigla

    def get_absolute_url(self):
        return reverse('uf_edit', kwargs={'pk': self.pk})


class Instituicao(models.Model):
    nome = models.CharField(max_length=200)
    uf = models.ForeignKey(UF, on_delete=models.SET_NULL, null=True)
    cep = models.IntegerField()
    logradouro = models.CharField(max_length=200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    municipio = models.CharField(max_length=200)
    fax = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    ramal = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    url = models.CharField(max_length=200)
    inicio = models.DateField()
    fim = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('instituicao_edit', kwargs={'pk': self.pk})
