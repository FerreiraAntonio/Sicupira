from django.db import models
from django.urls import reverse
from sicupira import models as SicupiraModel
from django.core.validators import MinValueValidator

##################################################
# Inicio do Bloco [Pessoa]
##################################################
from sicupira.models import Pais


class Pessoa(models.Model):
    nome =  SicupiraModel.CICharField(max_length=100)
    resumo = models.TextField(blank=True, null=True)
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

    email = SicupiraModel.CIEmailField(null=True, blank=True)
    nacionalidade = models.ForeignKey(SicupiraModel.Pais,
                                      on_delete=models.SET_NULL,
                                      null=True, blank=True,
                                      related_name='NacionalidadePessoa')

    lattes_id = models.CharField(max_length=45,blank=True, null=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('pessoa_edit', kwargs={'pk': self.pk})

    def fill_from_xml(self, pessoa_xml):
        self.nome = pessoa_xml["nome"]
        self.lattes_id = pessoa_xml["lattes_id"]
        print(self.lattes_id)
        self.resumo = pessoa_xml["resumo_cv"]

        if pessoa_xml["nacionalidade"]:
            self.nacionalidade = SicupiraModel.Pais.objects.get(pk=pessoa_xml["nacionalidade"])


##################################################
# Inicio do Bloco [Abreviatura]
##################################################
class Abreviatura(models.Model):
    desc_abreviatura = SicupiraModel.CICharField(max_length=100)
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
    programa = models.ForeignKey(SicupiraModel.Programa,
                                           on_delete=models.SET_NULL,
                                           null=True, blank=True,
                                           related_name='ProgramaDocente')
    categoria = models.ForeignKey(SicupiraModel.CategoriaDocente,
                                     on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='CategoriaDocente')
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
# class Vinculo(models.Model):
#     pessoa = models.ForeignKey(Docente,
#                                   on_delete=models.CASCADE,
#                                   related_name='Docente')
#     instituicao = models.ForeignKey(SicupiraModel.Instituicao,
#                                        on_delete=models.CASCADE,
#                                        related_name='Instituicao')
#     data_inicio = models.DateField()
#     categoria = models.ForeignKey(SicupiraModel.CategoriaDocente,
#                                      on_delete=models.SET_NULL,
#                                      null=True, blank=True,
#                                      related_name='CategoriaDocente')
# 
#     def __str__(self):
#         return '%s - %s' % (self.Docente.nome, self.Instituicao.nome)
# 
#     def get_absolute_url(self):
#         return reverse('vinculo_edit', kwargs={'pk': self.pk})


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
