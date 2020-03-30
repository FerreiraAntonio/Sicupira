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


###########################################################
# Bloco para Case inSensitive
###########################################################


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
# Inicio do Bloco [País]
##################################################


class Pais(models.Model):
    nome_pais = CICharField(max_length=100, unique=True)
    codigo_iso = CICharField(blank=True, null=True, max_length=3,  unique=True)
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
    nome = CICharField(max_length=50, unique=True)
    sigla = CICharField(max_length=2, unique=True)
    pais_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, related_name='PaisEstado')

    def __str__(self):
        return self.sigla

    def get_absolute_url(self):
        return reverse('estado_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Região]
##################################################


class Regiao(models.Model):
    desc_regiao = CICharField(max_length=60, unique=True)
    pais_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, related_name='PaisRegiao')

    def __str__(self):
        return self.desc_regiao

    def get_absolute_url(self):
        return reverse('regiao_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Área Avaliação]
##################################################


class AreaAvaliacao(models.Model):
    area_avaliacao = CICharField(max_length=60, unique=True)

    def __str__(self):
        return self.area_avaliacao

    def get_absolute_url(self):
        return reverse('areaavaliacao_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco AreaBasica
##################################################


class AreaBasica(models.Model):
    desc_area_basica = CICharField(max_length=60, unique=True)

    def __str__(self):
        return self.desc_area_basica

    def get_absolute_url(self):
        return reverse('areabasica_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Instituíção]
##################################################


class Instituicao(models.Model):
    nome = CICharField(max_length=100, unique=True)
    codigo_cnpq = CICharField(max_length=20, unique=True, null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('instituicao_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Nível Gradução]
##################################################


class NivelGraduacao(models.Model):
    desc_nivel_graduacao = CICharField(max_length=60, unique=True)

    def __str__(self):
        return self.desc_nivel_graduacao

    def get_absolute_url(self):
        return reverse('nivelgraduacao_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Tipo Documento]
##################################################


class TipoDocumento(models.Model):
    desc_tipo_doc = CICharField(max_length=45, unique=True)

    def __str__(self):
        return self.desc_tipo_doc

    def get_absolute_url(self):
        return reverse('tipodocumento_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Categoria Docente]
##################################################


class CategoriaDocente(models.Model):
    desc_categoria = CICharField(max_length=45, unique=True)

    def __str__(self):
        return self.desc_categoria

    def get_absolute_url(self):
        return reverse('categoriadocente_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Situação]
##################################################


class Situacao(models.Model):
    desc_situacao = CICharField(max_length=60, unique=True)

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
    desc_modalidade = CICharField(max_length=45, unique=True)

    def __str__(self):
        return self.desc_modalidade

    def get_absolute_url(self):
        return reverse('modalidade_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Sexo]
##################################################


class Sexo(models.Model):
    desc_sexo = CICharField(max_length=45, unique=True)

    def __str__(self):
        return self.desc_sexo

    def get_absolute_url(self):
        return reverse('sexo_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Nota]
##################################################


class Nota(models.Model):
    desc_nota = CICharField(max_length=45, unique=True)

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
    desc_situacao_matricula = CICharField(max_length=45, unique=True)

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
    desc_regime_letivo = CICharField(max_length=20, unique=True)

    def __str__(self):
        return self.desc_regime_letivo

    def get_absolute_url(self):
        return reverse('regimeletivo_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Período Letivo]
# pode ser : 1 até 6 em função do regime
##################################################


class PeriodoLetivo(models.Model):
    desc_periodo_letivo = CICharField(max_length=10)
    regime_letivo_id = models.ForeignKey(RegimeLetivo, on_delete=models.CheckConstraint, related_name='RegimePeriodoLetivo')

    def __str__(self):
        return self.desc_periodo_letivo

    def get_absolute_url(self):
        return reverse('periodoletivo_edit', kwargs={'pk': self.pk})


##################################################
# Inicio do Bloco [Programa]
##################################################


class Programa(models.Model):
    codigo_programa = CICharField(max_length=20, unique=True)
    nome_programa = CICharField(max_length=200, unique=True)
    nome_ingles = CICharField(max_length=200, unique=True)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.SET_NULL, null=True, related_name='NomeInstituicao')
    area_avaliacao = models.ForeignKey(AreaAvaliacao, on_delete=models.SET_NULL, null=True, related_name='AreaAvaliacao')
    nota = models.ForeignKey(Nota, on_delete=models.SET_NULL, null=True, related_name='NotaPrograma')
    flg_cooperacao = models.BooleanField(default=False)
    flg_rede = models.BooleanField(default=False)
    modalidade_id = models.ForeignKey(Modalidade, on_delete=models.SET_NULL, null=True, related_name='ModlidadePrograma')
    regime_letivo_id = models.ForeignKey(RegimeLetivo, on_delete=models.SET_NULL, null=True, related_name='RegimeLetivoPrograma')
    estado_id = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True, related_name='EstadoPrograma')
    regiao_id = models.ForeignKey(Regiao, on_delete=models.SET_NULL, null=True, related_name='RegiaoPrograma')
    situacao_id = models.ForeignKey(Situacao, on_delete=models.SET_NULL, null=True, related_name='SituacaoPrograma')
    area_basica = models.ForeignKey(AreaBasica, on_delete=models.SET_NULL, null=True, related_name='AreaBasica')

    def __str__(self):
        return '%s - %s' % (self.codigo_programa, self.nome_programa)

    def get_absolute_url(self):
        return reverse('programa_edit', kwargs={'pk': self.pk})


##################################################
# Inicio do Bloco [Area de Concentração]
##################################################


class AreaConcentracao(models.Model):
    desc_area_concentracao = CICharField(max_length=200, unique=True)
    programa_id = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name='Programa')

    def __str__(self):
        return self.desc_area_concentracao

    def get_absolute_url(self):
        return reverse('areaconcentracao_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco LinhaPesquisa
##################################################


class LinhaPesquisa(models.Model):
    nome_linha_pesquisa = CICharField(null=True, max_length=100, unique=True)    
    data_inicio = models.DateField(null=True)
    data_fim = models.DateField(null=True, blank=True)
    desc_linha_pesquisa = CITextField(null=True)
    area_concentracao_id = models.ForeignKey(AreaConcentracao, on_delete=models.SET_NULL, null=True, related_name='LinhaArea')

    def __str__(self):
        return self.nome_linha_pesquisa

    def get_absolute_url(self):
        return reverse('linhapesquisa_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Endereco]
##################################################


class EnderecoPrograma(models.Model):
    programa_id = models.ForeignKey(Programa,on_delete=models.CASCADE, related_name='ProgramaEndereco')
    estado_id = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    cep = models.IntegerField()
    logradouro = CICharField(max_length=200)
    numero = CICharField(max_length=20)
    complemento = CICharField(max_length=300, null=True, blank=True)
    bairro = CICharField(max_length=100)
    municipio = CICharField(max_length=100)
    fax = CICharField(max_length=20, null=True, blank=True)
    telefone = CICharField(max_length=20)
    ramal = CICharField(max_length=20, null=True, blank=True)
    email = CIEmailField(max_length=255, null=True, blank=True)
    web_site = CICharField(max_length=255,null=True, blank=True)
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
    numero = CICharField(max_length=10)
    ramal = CICharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return '%d - %s' % (self.ddd, self.numero)

    def get_absolute_url(self):
        return reverse('telefoneenderecoprograma_edit', kwargs={'pk': self.pk})

##################################################
# Inicio do Bloco [Curso]
##################################################


class Curso(models.Model):
    programa_id = models.ForeignKey(Programa, on_delete=models.SET_NULL, related_name='ProgramaCurso', null=True)
    nome_curso = CICharField(max_length=100, unique=True)
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
    nome_disciplina = CICharField(max_length=100, unique=True)
    sigla = CICharField(max_length=20, unique=True)
    numero = CICharField(max_length=450, unique=True)
    creditos = models.IntegerField(default=0)
    ementa = CITextField(blank=True, null=True)
    bibliografia = CITextField(blank=True, null=True)

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
    nome_turma = CICharField(max_length=45)
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
    desc_regime_trabalho = CICharField(max_length=45, unique=True)

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


class VinculoIES(models.Model):
    desc_vinculo_ies = CICharField(max_length=45, unique=True)

    def __str__(self):
        return self.desc_vinculo_ies

    def get_absolute_url(self):
        return reverse('vinculoies_edit', kwargs={'pk': self.pk})