from django.db import models
from django.urls import reverse
from sicupira import models as SicupiraModel


#######################
# CODE SMELL  :-)  Não sei importar de sicupira models.py
#######################
class CaseInsensitiveFieldMixin:

    LOOKUP_CONVERSIONS = {
        'exact': 'iexact',
        'contains': 'icontains',
        'startswith': 'istartswith',
        'endswith': 'iendswith',
        'regex': 'iregex',
    }

    def get_lookup(self, lookup_name):
        converted = self.LOOKUP_CONVERSIONS.get(lookup_name, lookup_name)
        return super().get_lookup(converted)


class CICharField(CaseInsensitiveFieldMixin, models.CharField):
    pass


class CIEmailField(CaseInsensitiveFieldMixin, models.EmailField):
    pass


class CITextField(CaseInsensitiveFieldMixin, models.TextField):
    pass


##################################################
# Inicio do Bloco [Pessoa]
##################################################

class Pessoa(models.Model):
    nome = CICharField(max_length=100)
    sexo = models.ForeignKey(SicupiraModel.Sexo,
                                      on_delete=models.SET_NULL,
                                      null=True, blank=True,
                                      related_name='SexoPessoa',
                                       default=1)

    data_nascimento = models.DateField()
    numero_documento = models.CharField(max_length=20)
    tipo_documento = models.ForeignKey(SicupiraModel.TipoDocumento,
                                      on_delete=models.SET_NULL,
                                      null=True, blank=True,
                                      related_name='TipoDoc',
                                       default=1)

    email = CIEmailField(null=True, blank=True)
    nacionalidade = models.ForeignKey(SicupiraModel.Pais,
                                      on_delete=models.SET_NULL,
                                      null=True, blank=True,
                                      related_name='NacionalidadePessoa')

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('pessoa_edit', kwargs={'pk': self.pk})


##################################################
# Inicio do Bloco [Abreviatura]
##################################################
class Abreviatura(models.Model):
    desc_abreviatura = CICharField(max_length=100)
    flg_principal = models.BooleanField(default=False)
    pessoa = models.ForeignKey(Pessoa,
                                  on_delete=models.CASCADE,
                                  related_name='Pessoa')

    def __str__(self):
        return self.desc_abreviatura

    def get_absolute_url(self):
        return reverse('abreviatura_edit', kwargs={'pk': self.pk})


##################################################
# Inicio do Bloco [Discente]
# OBS: Foi achatada com a classe Matricula Curso
##################################################
class Discente(models.Model):
    pessoa = models.OneToOneField(
        Pessoa,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='PessoaDiscente'
    )
    curso = models.ForeignKey(SicupiraModel.Curso,
                                 on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 related_name='Curso')
    situacao = models.ForeignKey(SicupiraModel.SituacaoMatricula,
                                    on_delete=models.SET_NULL,
                                    null=True, blank=True,
                                    related_name='SituacaoMatricula')
    data_situacao = models.DateField()
    nivel = models.ForeignKey(SicupiraModel.NivelGraduacao,
                                 on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 related_name='Nivel')

    def __str__(self):
        return self.pessoa.nome

    def get_absolute_url(self):
        return reverse('discente_edit', kwargs={'pk': self.pessoa.pk})


##################################################
# Inicio do Bloco [Docente]
##################################################
class Docente(models.Model):
    pessoa = models.OneToOneField(
        Pessoa,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='PessoaDocente'
    )
    titulo_nivel = models.ForeignKey(SicupiraModel.NivelGraduacao,
                                        on_delete=models.SET_NULL,
                                        null=True, blank=True,
                                        related_name='TituloNivel')
    data_titulacao = models.DateField()
    titulo_pais = models.ForeignKey(SicupiraModel.Pais,
                                       on_delete=models.SET_NULL,
                                       null=True, blank=True,
                                       related_name='TituloPais')
    regime_trabalho = models.ForeignKey(SicupiraModel.RegimeTrabalho,
                                           on_delete=models.SET_NULL,
                                           null=True, blank=True,
                                           related_name='RegimeTrabalhoDocente')
    vinculo_ies = models.ForeignKey(SicupiraModel.VinculoIES,
                                        on_delete=models.SET_NULL,
                                        null=True, blank=True,
                                        related_name='VinculoIESDocente')

    def __str__(self):
        return self.pessoa.nome

    def get_absolute_url(self):
        return reverse('docente_edit', kwargs={'pk': self.pessoa.pk})


##################################################
# Inicio do Bloco [Vinculo com Instituição]
##################################################
class Vinculo(models.Model):
    pessoa = models.ForeignKey(Docente,
                                  on_delete=models.CASCADE,
                                  related_name='Docente')
    instituicao = models.ForeignKey(SicupiraModel.Instituicao,
                                       on_delete=models.CASCADE,
                                       related_name='Instituicao')
    data_inicio = models.DateField()
    categoria = models.ForeignKey(SicupiraModel.CategoriaDocente,
                                     on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='CategoriaDocente')

    def __str__(self):
        return '%s - %s' % (self.Docente.nome, self.Instituicao.nome)

    def get_absolute_url(self):
        return reverse('vinculo_edit', kwargs={'pk': self.pk})


##################################################
# Inicio do Bloco [Orienta]
##################################################
class Orienta(models.Model):
    docente = models.ForeignKey(Docente,
                                   on_delete=models.CASCADE,
                                   related_name='DocenteOrienta')
    discente = models.ForeignKey(Discente,
                                    on_delete=models.CASCADE,
                                    related_name='DiscenteOrienta')
    data_orientacao = models.DateField()
    flg_principal = models.BooleanField(default=False)

    def __str__(self):
        return '%s - %s | $d' % (self.Dicente.nome, self.Docente.nome, self.flg_principal)

    def get_absolute_url(self):
        return reverse('orienta_edit', kwargs={'pk': self.pk})
