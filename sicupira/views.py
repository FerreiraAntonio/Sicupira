from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.core.paginator import Paginator

from sicupira.models import EnderecoPrograma as Endereco
from sicupira.models import Estado
from sicupira.models import LinhaPesquisa
from sicupira.models import Disciplina


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
# Inicio do Bloco [Endereco]
# by Antonio Horta
##################################################

@method_decorator(login_required(login_url='login'), name='dispatch')
class EnderecoList(ListView):
    paginate_by = 10
    model = Endereco

    def get_queryset(self):
        queryset = super(EnderecoList, self).get_queryset()
        queryset = queryset.order_by("nome")
        if 'estado' in self.request.GET:
            queryset = queryset.filter(estado__sigla__icontains=self.request.GET['estado'])
        if 'nome' in self.request.GET:
            queryset = queryset.filter(nome__icontains=self.request.GET['nome'])

        return queryset


@method_decorator(login_required(login_url='login'), name='dispatch')
class EnderecoView(DetailView):
    model = Endereco


@method_decorator(login_required(login_url='login'), name='dispatch')
class EnderecoCreate(CreateView):
    model = Endereco
    fields = ['nome', 'estado', 'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'municipio', 'fax', 'telefone', 'ramal', 'email', 'url', 'inicio', 'fim', 'latitude', 'longitude']
    success_url = reverse_lazy('endereco_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class EnderecoUpdate(UpdateView):
    model = Endereco
    fields = ['nome', 'estado', 'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'municipio', 'fax', 'telefone', 'ramal', 'email', 'url', 'inicio', 'fim', 'latitude', 'longitude']
    success_url = reverse_lazy('endereco_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class EnderecoDelete(DeleteView):
    model = Endereco
    success_url = reverse_lazy('endereco_list')

##################################################
# Fim do Bloco [Endereco]
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
# by Antonio Horta
##################################################


@method_decorator(login_required(login_url='login'), name='dispatch')
class LinhaPesquisaList(ListView):
    paginate_by = 10
    model = LinhaPesquisa

    def get_queryset(self):
        queryset = super(LinhaPesquisaList, self).get_queryset()
        queryset = queryset.order_by("desc_linha_pesquisa")
        if 'desc_linha_pesquisa' in self.request.GET:
            queryset = queryset.filter(desc_linha_pesquisa__icontains=self.request.GET['desc_linha_pesquisa'])

        return queryset


@method_decorator(login_required(login_url='login'), name='dispatch')
class LinhaPesquisaView(DetailView):
    model = LinhaPesquisa


@method_decorator(login_required(login_url='login'), name='dispatch')
class LinhaPesquisaCreate(CreateView):
    model = LinhaPesquisa
    fields = ['desc_linha_pesquisa']
    success_url = reverse_lazy('linhapesquisa_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class LinhaPesquisaUpdate(UpdateView):
    model = LinhaPesquisa
    fields = ['desc_linha_pesquisa']
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
