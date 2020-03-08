from django.db import models
from django.urls import reverse
from sicupira import models as SicupiraModel

##################################################
# Inicio do Bloco [Pessoa]
##################################################
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, default='M')
    data_nascimento = models.DateField()
    numero_documento = models.CharField(max_length=20)
    tipo_documento = models.DateField()
    email =  models.EmailField(null=True, blank=True)
    nacionalidade = models.ForeignKey(SicupiraModel.Pais, related_name='Nacionaludade')

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('pessoa_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Abreviatura]
##################################################
class Abreviatura(models.Model):
    desc_abreviatura = models.CharField(max_length=100)
    flg_principal = models.DateField(default=0)
    pessoa_id = models.ForeignKey(Pessoa, related_name='Pessoa')

    def __str__(self):
        return self.desc_abreviatura

    def get_absolute_url(self):
        return reverse('abreviatura_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Discente]
# OBS: Foi achatada com a classe Matricula Curso
##################################################
class Discente(models.Model):
    pessoa_id = models.OneToOneField(
        Pessoa,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    curso_id = models.ForeignKey(SicupiraModel.Curso, primary_key=True, related_name='Curso')
    situacao_id = models.ForeignKey(SicupiraModel.SituacaoMatricula, related_name='SituacaoMatricula')
    data_situacao = models.DateField()
    nivel_id = models.ForeignKey(SicupiraModel.NivelGraduacao, related_name='Nivel')

    def __str__(self):
        return '%s - %s' % (self.Pessoa.nome, self.Curso.nome_curso)

    def __str__(self):
        return self.Pessoa.nome
    def get_absolute_url(self):
        return reverse('discente_edit', kwargs={'pk': self.pk})


##################################################
# Inicio do Bloco [Docente]
##################################################
class Docente(models.Model):
    pessoa_id = models.OneToOneField(
        Pessoa,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    titulo_nivel_id = models.ForeignKey(SicupiraModel.NivelGraduacao, related_name='TituloNivel')
    data_titulacao = models.DateField()
    titulo_pais_id = models.ForeignKey(SicupiraModel.Pais, on_delete=models.SET_NULL, related_name='TituloPais')
    regime_trabalho_id = models.ForeignKey(SicupiraModel.RegimeTrabalho, on_delete=models.SET_NULL, related_name='RegimeTrabalhoDocente')
    vinclulo_ies_id = models.ForeignKey(SicupiraModel.VincluloIES, on_delete=models.SET_NULL, related_name='VincluloIESDocente')

    def __str__(self):
        return self.Pessoa.nome
    def get_absolute_url(self):
        return reverse('docente_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Vinculo com Instituição]
##################################################
class Vinculo(models.Model):
    pessoa_id = models.ForeignKey(Docente, primary_key=True, related_name='Docente')
    instituicao_id = models.ForeignKey(SicupiraModel.Instituicao, primary_key=True, related_name='Instituicao')
    data_inicio = models.DateField()
    categoria_id = models.ForeignKey(SicupiraModel.CategoriaDocente, related_name='CategoriaDocente')

    def __str__(self):
        return '%s - %s' % (self.Docente.nome, self.Instituicao.nome)

    def get_absolute_url(self):
        return reverse('vinculo_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Orienta]
##################################################
class Orienta(models.Model):
    docente_id = models.ForeignKey(Docente, primary_key=True, related_name='Docente')
    discente_id = models.ForeignKey(Discente, primary_key=True, related_name='Discente')
    data_orientacao = models.DateField()
    flg_principal =  models.IntegerField(default=0)

    def __str__(self):
        return '%s - %s | $d' % (self.Dicente.nome, self.Docente.nome, self.flg_principal)

    def get_absolute_url(self):
        return reverse('orienta_edit', kwargs={'pk': self.pk})