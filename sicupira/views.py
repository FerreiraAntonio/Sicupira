from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.core.paginator import Paginator

from sicupira.models import EnderecoPrograma as Endereco
from sicupira.models import Estado as UF

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
        if 'uf' in self.request.GET:
            queryset = queryset.filter(uf__sigla__icontains=self.request.GET['uf'])
        if 'nome' in self.request.GET:
            queryset = queryset.filter(nome__icontains=self.request.GET['nome'])

        return queryset


@method_decorator(login_required(login_url='login'), name='dispatch')
class EnderecoView(DetailView):
    model = Endereco


@method_decorator(login_required(login_url='login'), name='dispatch')
class EnderecoCreate(CreateView):
    model = Endereco
    fields = ['nome', 'uf', 'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'municipio', 'fax', 'telefone', 'ramal', 'email', 'url', 'inicio', 'fim', 'latitude', 'longitude']
    success_url = reverse_lazy('endereco_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class EnderecoUpdate(UpdateView):
    model = Endereco
    fields = ['nome', 'uf', 'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'municipio', 'fax', 'telefone', 'ramal', 'email', 'url', 'inicio', 'fim', 'latitude', 'longitude']
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
class UFList(ListView):
    paginate_by = 10
    model = UF

    def get_queryset(self):
        queryset = super(UFList, self).get_queryset()
        queryset = queryset.order_by("nome")
        if 'sigla' in self.request.GET:
            queryset = queryset.filter(sigla__icontains=self.request.GET['sigla'])
        if 'nome' in self.request.GET:
            queryset = queryset.filter(nome__icontains=self.request.GET['nome'])

        return queryset


@method_decorator(login_required(login_url='login'), name='dispatch')
class UFView(DetailView):
    model = UF


@method_decorator(login_required(login_url='login'), name='dispatch')
class UFCreate(CreateView):
    model = UF
    fields = ['nome', 'sigla']
    success_url = reverse_lazy('uf_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class UFUpdate(UpdateView):
    model = UF
    fields = ['nome', 'sigla']
    success_url = reverse_lazy('uf_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class UFDelete(DeleteView):
    model = UF
    success_url = reverse_lazy('uf_list')

##################################################
# Fim do Bloco [UF]
##################################################
