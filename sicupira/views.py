from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.core.paginator import Paginator

from sicupira.models import EnderecoPrograma
from sicupira.models import Estado
from sicupira.models import LinhaPesquisa
from sicupira.models import Disciplina
from sicupira.models import Turma
from sicupira.models import Programa
from sicupira.models import Curso


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def index(request):
    if request.user.is_authenticated:
        return render(request, 'sicupira/index.html', {})
    else:
        return redirect('login')


def importaxml(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'sicupira/importaxml.html', {
                'uploaded_file_url': uploaded_file_url
            })
        return render(request, 'sicupira/importaxml.html', {})
    else:
        return redirect('login')


##################################################
# ATENÇÃO: CADA DESENVOLVEDOR DEVE DUPLICAR      #
# UM BLOCO PARA CADA CLASSE. PARA ISSO BASTA     #
# COPIAR, COLAR E DEPOIS RENOMEAR A CLASSE PARA  #
# O NOME DA NOVA CLASSE.                         #
##################################################


##################################################
# Inicio do Bloco [EnderecoPrograma]
# by Antonio Horta
# programa_id = models.ForeignKey(Programa,on_delete=models.CASCADE, related_name='ProgramaEndereco')
# estado_id = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
# cep = models.IntegerField()
# logradouro = models.CharField(max_length=200)
# numero = models.CharField(max_length=20)
# complemento = models.CharField(max_length=300, null=True, blank=True)
# bairro = models.CharField(max_length=100)
# municipio = models.CharField(max_length=100)
# fax = models.CharField(max_length=20)
# telefone = models.CharField(max_length=20)
# ramal = models.CharField(max_length=20)
# email = models.EmailField(max_length=255, null=True, blank=True)
# web_site = models.CharField(max_length=255,null=True, blank=True)
# inicio = models.DateField()
# fim = models.DateField()
# latitude = models.FloatField()
# longitude = models.FloatField()
##################################################


@method_decorator(login_required(login_url='login'), name='dispatch')
class EnderecoProgramaList(ListView):
    paginate_by = 10
    model = EnderecoPrograma

    def get_queryset(self):
        queryset = super(EnderecoProgramaList, self).get_queryset()
        queryset = queryset.order_by("logradouro")
        if 'estado' in self.request.GET:
            queryset = queryset.filter(estado__sigla__icontains=self.request.GET['estado'])
        if 'logradouro' in self.request.GET:
            queryset = queryset.filter(logradouro__icontains=self.request.GET['logradouro'])
        if 'programa' in self.request.GET:
            queryset = queryset.filter(programa_id__nome_programa__icontains=self.request.GET['programa'])

        return queryset


@method_decorator(login_required(login_url='login'), name='dispatch')
class EnderecoProgramaView(DetailView):
    model = EnderecoPrograma


@method_decorator(login_required(login_url='login'), name='dispatch')
class EnderecoProgramaCreate(CreateView):
    model = EnderecoPrograma
    fields = ['programa_id', 'estado_id', 'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'municipio', 'fax', 'telefone', 'ramal', 'email', 'web_site', 'inicio', 'fim', 'latitude', 'longitude']
    success_url = reverse_lazy('enderecoprograma_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class EnderecoProgramaUpdate(UpdateView):
    model = EnderecoPrograma
    fields = ['programa_id', 'estado_id', 'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'municipio', 'fax', 'telefone', 'ramal', 'email', 'web_site', 'inicio', 'fim', 'latitude', 'longitude']
    success_url = reverse_lazy('enderecoprograma_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class EnderecoProgramaDelete(DeleteView):
    model = EnderecoPrograma
    success_url = reverse_lazy('enderecoprograma_list')

##################################################
# Fim do Bloco [EnderecoPrograma]
##################################################


##################################################
# Inicio do Bloco [Curso]
# by Antonio Horta
# programa_id = models.ForeignKey(Programa, on_delete=models.SET_NULL, related_name='ProgramaCurso', null=True)
# nome_curso = models.CharField(max_length=100, unique=True)
# nivel_id = models.ForeignKey(NivelGraduacao, on_delete=models.SET_NULL, related_name='NivelCurso', null=True)
# situacao_id = models.ForeignKey(Situacao, on_delete=models.SET_NULL, related_name='SituacaoCurso', null=True)
# creditos_titulacao = models.IntegerField(default=0)
# disciplina = models.IntegerField(default=0)
# trabalho_conclusao = models.IntegerField(default=0)
# outros = models.IntegerField(default=0)
# equivalencia_hora = models.IntegerField(default=0)
##################################################


@method_decorator(login_required(login_url='login'), name='dispatch')
class CursoList(ListView):
    paginate_by = 10
    model = Curso

    def get_queryset(self):
        queryset = super(CursoList, self).get_queryset()
        queryset = queryset.order_by("nome_curso")
        if 'nome' in self.request.GET:
            queryset = queryset.filter(nome_curso__icontains=self.request.GET['nome'])
        if 'programa' in self.request.GET:
            queryset = queryset.filter(programa_id__nome_programa__icontains=self.request.GET['programa'])

        return queryset


@method_decorator(login_required(login_url='login'), name='dispatch')
class CursoView(DetailView):
    model = Curso


@method_decorator(login_required(login_url='login'), name='dispatch')
class CursoCreate(CreateView):
    model = Curso
    fields = ['programa_id', 'nome_curso', 'nivel_id', 'situacao_id', 'creditos_titulacao', 'disciplina', 'trabalho_conclusao', 'outros', 'equivalencia_hora']
    success_url = reverse_lazy('curso_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class CursoUpdate(UpdateView):
    model = Curso
    fields = ['programa_id', 'nome_curso', 'nivel_id', 'situacao_id', 'creditos_titulacao', 'disciplina', 'trabalho_conclusao', 'outros', 'equivalencia_hora']
    success_url = reverse_lazy('curso_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class CursoDelete(DeleteView):
    model = Curso
    success_url = reverse_lazy('curso_list')

##################################################
# Fim do Bloco [Curso]
##################################################


##################################################
# Inicio do Bloco [UF]
# by Antonio Horta
##################################################


@method_decorator(login_required(login_url='login'), name='dispatch')
class EstadoList(ListView):
    paginate_by = 10
    model = Estado

    def get_queryset(self):
        queryset = super(EstadoList, self).get_queryset()
        queryset = queryset.order_by("nome")
        if 'sigla' in self.request.GET:
            queryset = queryset.filter(sigla__icontains=self.request.GET['sigla'])
        if 'nome' in self.request.GET:
            queryset = queryset.filter(nome__icontains=self.request.GET['nome'])

        return queryset


@method_decorator(login_required(login_url='login'), name='dispatch')
class EstadoView(DetailView):
    model = Estado


@method_decorator(login_required(login_url='login'), name='dispatch')
class EstadoCreate(CreateView):
    model = Estado
    fields = ['nome', 'sigla']
    success_url = reverse_lazy('estado_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class EstadoUpdate(UpdateView):
    model = Estado
    fields = ['nome', 'sigla']
    success_url = reverse_lazy('estado_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class EstadoDelete(DeleteView):
    model = Estado
    success_url = reverse_lazy('estado_list')

##################################################
# Fim do Bloco [UF]
##################################################


##################################################
# Inicio do Bloco [LinhaPesquisa]
# by Guilherme Bernieri
##################################################


@method_decorator(login_required(login_url='login'), name='dispatch')
class LinhaPesquisaList(ListView):
    paginate_by = 10
    model = LinhaPesquisa

    def get_queryset(self):
        queryset = super(LinhaPesquisaList, self).get_queryset()
        queryset = queryset.order_by("nome_linha_pesquisa")
        if 'nome_linha_pesquisa' in self.request.GET:
            queryset = queryset.filter(nome_linha_pesquisa__icontains=self.request.GET['nome_linha_pesquisa'])
        if 'instituicao' in self.request.GET:
            queryset = queryset.filter(area_concentracao_id__programa_id__instituicao__nome__icontains=self.request.GET['instituicao'])
        if 'programa' in self.request.GET:
            queryset = queryset.filter(area_concentracao_id__programa_id__nome_programa__icontains=self.request.GET['programa'])
        if 'data_inicio' in self.request.GET:
            queryset = queryset.filter(data_inicio__icontains=self.request.GET['data_inicio'])
        return queryset


@method_decorator(login_required(login_url='login'), name='dispatch')
class LinhaPesquisaView(DetailView):
    model = LinhaPesquisa


@method_decorator(login_required(login_url='login'), name='dispatch')
class LinhaPesquisaCreate(CreateView):
    model = LinhaPesquisa
    fields = ['nome_linha_pesquisa', 'data_inicio', 'data_fim', 'desc_linha_pesquisa', 'area_concentracao_id']
    success_url = reverse_lazy('linhapesquisa_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class LinhaPesquisaUpdate(UpdateView):
    model = LinhaPesquisa
    fields = ['nome_linha_pesquisa', 'data_inicio', 'data_fim', 'desc_linha_pesquisa', 'area_concentracao_id']
    success_url = reverse_lazy('linhapesquisa_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class LinhaPesquisaDelete(DeleteView):
    model = LinhaPesquisa
    success_url = reverse_lazy('linhapesquisa_list')

##################################################
# Fim do Bloco [LinhaPesquisa]
##################################################

##################################################
# Inicio do Bloco [Disciplina]
# by Antonio Horta
# nome_disciplina = models.CharField(max_length=100, unique=True)
# sigla = models.CharField(max_length=20, unique=True)
# numero = models.CharField(max_length=450, unique=True)
# creditos = models.IntegerField(default=0)
# ementa = models.TextField(blank=True, null=True)
# bibliografia = models.TextField(blank=True, null=True)
##################################################

@method_decorator(login_required(login_url='login'), name='dispatch')
class DisciplinaList(ListView):
    paginate_by = 10
    model = Disciplina

    def get_queryset(self):
        queryset = super(DisciplinaList, self).get_queryset()
        queryset = queryset.order_by("nome_disciplina")
        if 'sigla' in self.request.GET:
            queryset = queryset.filter(sigla__icontains=self.request.GET['sigla'])
        if 'nome_disciplina' in self.request.GET:
            queryset = queryset.filter(nome_disciplina__icontains=self.request.GET['nome_disciplina'])

        return queryset


@method_decorator(login_required(login_url='login'), name='dispatch')
class DisciplinaView(DetailView):
    model = Disciplina


@method_decorator(login_required(login_url='login'), name='dispatch')
class DisciplinaCreate(CreateView):
    model = Disciplina
    fields = ['nome_disciplina', 'sigla', 'numero', 'creditos', 'ementa', 'bibliografia']
    success_url = reverse_lazy('disciplina_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class DisciplinaUpdate(UpdateView):
    model = Disciplina
    fields = ['nome_disciplina', 'sigla', 'numero', 'creditos', 'ementa', 'bibliografia']
    success_url = reverse_lazy('disciplina_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class DisciplinaDelete(DeleteView):
    model = Disciplina
    success_url = reverse_lazy('disciplina_list')

##################################################
# Fim do Bloco [Disciplina]
##################################################


##################################################
# Inicio do Bloco [Turma]
# by Antonio Horta
# curso_id = models.ForeignKey(Curso, on_delete=models.CheckConstraint, related_name='TurmaCurso')
# disciplina_id = models.ForeignKey(Disciplina, on_delete=models.CheckConstraint, related_name='TurmaDiscipliana')
# ano = models.IntegerField(default=0)
# periodo_letivo_id = models.ForeignKey(PeriodoLetivo, on_delete=models.CheckConstraint, related_name='TurmaPeriodoLeitivo')
##################################################

@method_decorator(login_required(login_url='login'), name='dispatch')
class TurmaList(ListView):
    paginate_by = 10
    model = Turma

    def get_queryset(self):
        queryset = super(TurmaList, self).get_queryset()
        queryset = queryset.order_by("nome_turma")
        if 'nome' in self.request.GET:
            queryset = queryset.filter(nome_turma__icontains=self.request.GET['nome'])
        if 'instituicao' in self.request.GET:
            queryset = queryset.filter(curso_id__programa_id__instituicao__nome__icontains=self.request.GET['instituicao'])
        if 'programa' in self.request.GET:
            queryset = queryset.filter(curso_id__programa_id__nome_programa__icontains=self.request.GET['programa'])
        if 'ano' in self.request.GET:
            queryset = queryset.filter(ano=self.request.GET['ano'])
        return queryset


@method_decorator(login_required(login_url='login'), name='dispatch')
class TurmaView(DetailView):
    model = Turma


@method_decorator(login_required(login_url='login'), name='dispatch')
class TurmaCreate(CreateView):
    model = Turma
    fields = ['nome_turma', 'curso_id', 'disciplina_id', 'ano', 'periodo_letivo_id']
    success_url = reverse_lazy('turma_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class TurmaUpdate(UpdateView):
    model = Turma
    fields = ['nome_turma', 'curso_id', 'disciplina_id', 'ano', 'periodo_letivo_id']
    success_url = reverse_lazy('turma_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class TurmaDelete(DeleteView):
    model = Turma
    success_url = reverse_lazy('turma_list')

##################################################
# Fim do Bloco [Turma]
##################################################


##################################################
# Inicio do Bloco [Programa]
# by Antonio Horta
# codigo_programa = models.CharField(max_length=20, unique=True)
# nome_programa = models.CharField(max_length=200, unique=True)
# nome_ingles = models.CharField(max_length=200, unique=True)
# nota = models.ForeignKey(Nota, on_delete=models.SET_NULL, null=True, related_name='NotaPrograma')
# flg_cooperacao = models.IntegerField(default=0)
# flg_rede = models.IntegerField(default=0)
# modalidade_id = models.ForeignKey(Modalidade, on_delete=models.SET_NULL, null=True, related_name='ModlidadePrograma')
# regime_letivo_id = models.ForeignKey(RegimeLetivo, on_delete=models.SET_NULL, null=True, related_name='RegimeLetivoPrograma')
# estado_id = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True, related_name='EstadoPrograma')
# regiao_id = models.ForeignKey(Regiao, on_delete=models.SET_NULL, null=True, related_name='RegiaoPrograma')
# situacao_id = models.ForeignKey(Situacao, on_delete=models.SET_NULL, null=True, related_name='SituacaoPrograma')
# linha_pesquisa_id = models.ForeignKey(LinhaPesquisa, on_delete=models.SET_NULL, null=True, related_name='LinhaPesquisaPrograma')
##################################################


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProgramaList(ListView):
    paginate_by = 10
    model = Programa

    def get_queryset(self):
        queryset = super(ProgramaList, self).get_queryset()
        queryset = queryset.order_by("nome_programa")
        if 'codigo_programa' in self.request.GET:
            queryset = queryset.filter(codigo_programa__icontains=self.request.GET['codigo_programa'])
        if 'nome_programa' in self.request.GET:
            queryset = queryset.filter(nome_programa__icontains=self.request.GET['nome_programa'])
        if 'instituicao' in self.request.GET:
            queryset = queryset.filter(instituicao__nome__icontains=self.request.GET['instituicao'])
        if 'areabasica' in self.request.GET:
            queryset = queryset.filter(area_basica__desc_area_basica__icontains=self.request.GET['areabasica'])
        if 'areaavaliacao' in self.request.GET:
            queryset = queryset.filter(area_avaliacao__area_avaliacao__icontains=self.request.GET['areaavaliacao'])
        if 'nota' in self.request.GET:
            queryset = queryset.filter(nota__desc_nota__icontains=self.request.GET['nota'])
        if 'situacao' in self.request.GET:
            queryset = queryset.filter(situacao_id__desc_situacao__icontains=self.request.GET['situacao'])
        if 'modalidade' in self.request.GET:
            queryset = queryset.filter(modalidade_id__desc_modalidade__icontains=self.request.GET['modalidade'])
        if 'regiao' in self.request.GET:
            queryset = queryset.filter(regiao_id__desc_regiao__icontains=self.request.GET['regiao'])
        if 'sigla' in self.request.GET:
            queryset = queryset.filter(estado_id__sigla__icontains=self.request.GET['sigla'])
        if 'cooperacao' in self.request.GET:
            queryset = queryset.filter(flg_cooperacao__icontains=self.request.GET['cooperacao'])
        if 'rede' in self.request.GET:
            queryset = queryset.filter(flg_rede__icontains=self.request.GET['rede'])

        return queryset


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProgramaView(DetailView):
    model = Programa


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProgramaCreate(CreateView):
    model = Programa
    fields = ['codigo_programa', 'nome_programa', 'nome_ingles', 'nota', 'flg_cooperacao', 'flg_rede', 'modalidade_id', 'regime_letivo_id', 'estado_id', 'regiao_id', 'situacao_id', 'instituicao', 'area_avaliacao', 'area_basica']
    success_url = reverse_lazy('programa_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProgramaUpdate(UpdateView):
    model = Programa
    fields = ['codigo_programa', 'nome_programa', 'nome_ingles', 'nota', 'flg_cooperacao', 'flg_rede', 'modalidade_id', 'regime_letivo_id', 'estado_id', 'regiao_id', 'situacao_id', 'instituicao', 'area_avaliacao', 'area_basica']
    success_url = reverse_lazy('programa_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProgramaDelete(DeleteView):
    model = Programa
    success_url = reverse_lazy('programa_list')

##################################################
# Fim do Bloco [Programa]
##################################################
