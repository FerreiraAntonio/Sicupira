from django.db import models
from django.urls import reverse

###########################################################
# ATENÇÃO: CADA DESENVOLVEDOR DEVE DUPLICAR               #
# UM BLOCO PARA CADA CLASSE E RENOMEAR PARA               #
# O NOME DA NOVA CLASSE.                                  #
# A ESTRUTURA DEVE RESPEITAR AS REGRAS                    #
# DO MODELO DE DADOS DO SISTEMA QUE ESTA NO WIKI          #
# Mais informações sobre modelagem python:                #
# https://docs.djangoproject.com/en/3.0/topics/db/models/ #
###########################################################

##################################################
# Inicio do Bloco [País]
##################################################


class Pais(models.Model):
    nome_pais = models.CharField(max_length=100, unique=True)
    codigo_iso = models.CharField(blank=True, null=True, max_length=3,  unique=True)
    ddd = models.IntegerField(blank=True)

    def __str__(self):
        return self.nome_pais

    def get_absolute_url(self):
        return reverse('pais_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [UF]
# by Antonio Horta
##################################################


class Estado(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    sigla = models.CharField(max_length=2, unique=True)
    pais_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, related_name='PaisEstado')

    def __str__(self):
        return self.sigla

    def get_absolute_url(self):
        return reverse('estado_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Região]
##################################################


class Regiao(models.Model):
    desc_regiao = models.CharField(max_length=60, unique=True)
    pais_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, related_name='PaisRegiao')

    def __str__(self):
        return self.desc_regiao

    def get_absolute_url(self):
        return reverse('regiao_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Área Avaliação]
##################################################


class AreaAvaliacao(models.Model):
    area_avaliacao = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.area_avaliacao

    def get_absolute_url(self):
        return reverse('areaavaliacao_edit', kwargs={'pk': self.pk})


##################################################
# Inicio do Bloco LinhaPesquisa Antigo [Área Base]
##################################################


class LinhaPesquisa(models.Model):
    desc_linha_pesquisa = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.desc_linha_pesquisa

    def get_absolute_url(self):
        return reverse('linhapesquisa_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Instituíção]
##################################################


class Instituicao(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    codigo_cnpq = models.CharField(max_length=20, unique=True, null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('instituicao_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Nível Gradução]
##################################################


class NivelGraduacao(models.Model):
    desc_nivel_graduacao = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.desc_nivel_graduacao

    def get_absolute_url(self):
        return reverse('nivelgraduacao_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Tipo Documento]
##################################################


class TipoDocumento(models.Model):
    desc_tipo_doc = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.desc_tipo_doc

    def get_absolute_url(self):
        return reverse('tipodocumento_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Categoria Docente]
##################################################


class CategoriaDocente(models.Model):
    desc_categoria = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.desc_categoria

    def get_absolute_url(self):
        return reverse('categoriadocente_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Situação]
##################################################


class Situacao(models.Model):
    desc_situacao = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.desc_situacao

    def get_absolute_url(self):
        return reverse('situacao_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Modalidade]
# pode ser:
#  1- Acadêmico
#  2- Profissional
##################################################


class Modalidade(models.Model):
    desc_modalidade = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.desc_modalidade

    def get_absolute_url(self):
        return reverse('modalidade_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Sexo]
##################################################


class Sexo(models.Model):
    desc_sexo = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.desc_sexo

    def get_absolute_url(self):
        return reverse('sexo_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Nota]
##################################################


class Nota(models.Model):
    desc_nota = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.desc_nota

    def get_absolute_url(self):
        return reverse('nota_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [SituacaoMatricula]
# pode ser:
# 1- Matriculado
# 2- Abandonou
# 3- Desligado
# 4- Mudança de nível sem defesa
##################################################


class SituacaoMatricula(models.Model):
    desc_situacao_matricula = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.desc_situacao_matricula

    def get_absolute_url(self):
        return reverse('situacaomatricula_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Regime Letivo]
# pode ser:
#  1- Anual
#  2- Bimestral
#  3- Quadrimestral
#  4- Trimestral
##################################################


class RegimeLetivo(models.Model):
    desc_regime_letivo = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.desc_regime_letivo

    def get_absolute_url(self):
        return reverse('regimeletivo_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Período Letivo]
# pode ser : 1 até 6 em função do regime
##################################################


class PeriodoLetivo(models.Model):
    desc_periodo_letivo = models.CharField(max_length=10)
    regime_letivo_id = models.ForeignKey(RegimeLetivo, on_delete=models.CheckConstraint, related_name='RegimePeriodoLetivo')

    def __str__(self):
        return self.desc_periodo_letivo

    def get_absolute_url(self):
        return reverse('periodoletivo_edit', kwargs={'pk': self.pk})


##################################################
# Inicio do Bloco [Programa]
##################################################


class Programa(models.Model):
    codigo_programa = models.CharField(max_length=20, unique=True)
    nome_programa = models.CharField(max_length=200, unique=True)
    nome_ingles = models.CharField(max_length=200, unique=True)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.SET_NULL, null=True, related_name='NomeInstituicao')
    area_avaliacao = models.ForeignKey(AreaAvaliacao, on_delete=models.SET_NULL, null=True, related_name='AreaAvaliacao')
    nota = models.ForeignKey(Nota, on_delete=models.SET_NULL, null=True, related_name='NotaPrograma')
    flg_cooperacao = models.IntegerField(default=0)
    flg_rede = models.IntegerField(default=0)
    modalidade_id = models.ForeignKey(Modalidade, on_delete=models.SET_NULL, null=True, related_name='ModlidadePrograma')
    regime_letivo_id = models.ForeignKey(RegimeLetivo, on_delete=models.SET_NULL, null=True, related_name='RegimeLetivoPrograma')
    estado_id = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True, related_name='EstadoPrograma')
    regiao_id = models.ForeignKey(Regiao, on_delete=models.SET_NULL, null=True, related_name='RegiaoPrograma')
    situacao_id = models.ForeignKey(Situacao, on_delete=models.SET_NULL, null=True, related_name='SituacaoPrograma')
    linha_pesquisa_id = models.ForeignKey(LinhaPesquisa, on_delete=models.SET_NULL, null=True, related_name='LinhaPesquisaPrograma')

    def __str__(self):
        return '%s - %s' % (self.codigo_programa, self.nome_programa)

    def get_absolute_url(self):
        return reverse('programa_edit', kwargs={'pk': self.pk})


##################################################
# Inicio do Bloco [Area de Concentração]
##################################################


class AreaConcentracao(models.Model):
    desc_area_concentracao = models.CharField(max_length=200, unique=True)
    programa_id = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name='Programa')

    def __str__(self):
        return self.desc_area_concentracao

    def get_absolute_url(self):
        return reverse('areaconcentracao_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Endereco]
##################################################


class EnderecoPrograma(models.Model):
    programa_id = models.ForeignKey(Programa,on_delete=models.CASCADE, related_name='ProgramaEndereco')
    estado_id = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    cep = models.IntegerField()
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=300, null=True, blank=True)
    bairro = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    fax = models.CharField(max_length=20, null=True, blank=True)
    telefone = models.CharField(max_length=20)
    ramal = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    web_site = models.CharField(max_length=255,null=True, blank=True)
    inicio = models.DateField()
    fim = models.DateField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return '%s, %d' % (self.logradouro, self.numero)

    def get_absolute_url(self):
        return reverse('enderecoprograma_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Telefone Endereco Programa]
##################################################


class TelefoneEnderecoPrograma(models.Model):
    endereco_id = models.ForeignKey(EnderecoPrograma, on_delete=models.CASCADE, related_name='EnderecoTelefone')
    tipo = models.IntegerField()
    ddd = models.IntegerField()
    numero = models.CharField(max_length=10)
    ramal = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return '%d - %s' % (self.ddd, self.numero)

    def get_absolute_url(self):
        return reverse('telefoneenderecoprograma_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Curso]
##################################################


class Curso(models.Model):
    programa_id = models.ForeignKey(Programa, on_delete=models.SET_NULL, related_name='ProgramaCurso', null=True)
    nome_curso = models.CharField(max_length=100, unique=True)
    nivel_id = models.ForeignKey(NivelGraduacao, on_delete=models.SET_NULL, related_name='NivelCurso', null=True)
    situacao_id = models.ForeignKey(Situacao, on_delete=models.SET_NULL, related_name='SituacaoCurso', null=True)
    creditos_titulacao = models.IntegerField(default=0)
    disciplina = models.IntegerField(default=0)
    trabalho_conclusao = models.IntegerField(default=0)
    outros = models.IntegerField(default=0)
    equivalencia_hora = models.IntegerField(default=0)

    def __str__(self):
        return self.nome_curso

    def get_absolute_url(self):
        return reverse('curso_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Disciplina]
##################################################


class Disciplina(models.Model):
    nome_disciplina = models.CharField(max_length=100, unique=True)
    sigla = models.CharField(max_length=20, unique=True)
    numero = models.CharField(max_length=450, unique=True)
    creditos = models.IntegerField(default=0)
    ementa = models.TextField(blank=True, null=True)
    bibliografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome_disciplina

    def get_absolute_url(self):
        return reverse('disciplina_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [CursoxDisciplina]
##################################################


class CursoxDisciplina(models.Model):
    curso_id =  models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='CursoCursoxDiscipliana')
    disciplina_id = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='DisciplinaCursoxDiscipliana')
    carga_horaria = models.IntegerField(default=0)

    def __str__(self):
        return '%s - %s' % (self.curso_id, self.disciplina_id)


##################################################
# Inicio do Bloco [AreaConcentracaoxDisciplina]
##################################################


class AreaConcentracaoxDisciplina(models.Model):
    area_concentracao_id =  models.ForeignKey(AreaConcentracao, on_delete=models.CASCADE, related_name='AreaAreaConcentracaoxDisciplina')
    disciplina_id = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='DisciplinaAreaConcentracaoxDisciplina')

    def __str__(self):
        return '%s - %s' % (self.area_concentracao_id, self.disciplina_id)

##################################################
# Inicio do Bloco [Turma]
##################################################


class Turma(models.Model):
    nome_turma = models.CharField(max_length=45)
    curso_id = models.ForeignKey(Curso, on_delete=models.CheckConstraint, related_name='TurmaCurso')
    disciplina_id = models.ForeignKey(Disciplina, on_delete=models.CheckConstraint, related_name='TurmaDiscipliana')
    ano = models.IntegerField(default=0)
    periodo_letivo_id = models.ForeignKey(PeriodoLetivo, on_delete=models.CheckConstraint, related_name='TurmaPeriodoLeitivo')

    def __str__(self):
        return self.nome_turma

    def get_absolute_url(self):
        return reverse('turma_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [RegimeTrabalho]
# pode ser :
# 1- Dedicação Exclusiva
# 2- Parcial
##################################################


class RegimeTrabalho(models.Model):
    desc_regime_trabalho = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.desc_regime_trabalho

    def get_absolute_url(self):
        return reverse('descregimetrabalho_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [VincluloIES]
# pode ser:
# 1- Servidor Público/CLT
# 2- Aposentado
# 3- Bolsa de fixação
# 4- Colaborador
##################################################


class VincluloIES(models.Model):
    desc_vinclulo_ies = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.desc_vinclulo_ies

    def get_absolute_url(self):
        return reverse('vincluloies_edit', kwargs={'pk': self.pk})