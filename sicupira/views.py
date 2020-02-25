from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.core.paginator import Paginator

from sicupira.models import Endereco
from sicupira.models import UF


def index(request):
    return render(request, 'sicupira/index.html', {})

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


class EnderecoView(DetailView):
    model = Endereco


class EnderecoCreate(CreateView):
    model = Endereco
    fields = ['nome', 'uf', 'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'municipio', 'fax', 'telefone', 'ramal', 'email', 'url', 'inicio', 'fim', 'latitude', 'longitude']
    success_url = reverse_lazy('endereco_list')


class EnderecoUpdate(UpdateView):
    model = Endereco
    fields = ['nome', 'uf', 'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'municipio', 'fax', 'telefone', 'ramal', 'email', 'url', 'inicio', 'fim', 'latitude', 'longitude']
    success_url = reverse_lazy('endereco_list')


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


class UFView(DetailView):
    model = UF


class UFCreate(CreateView):
    model = UF
    fields = ['nome', 'sigla']
    success_url = reverse_lazy('uf_list')


class UFUpdate(UpdateView):
    model = UF
    fields = ['nome', 'sigla']
    success_url = reverse_lazy('uf_list')


class UFDelete(DeleteView):
    model = UF
    success_url = reverse_lazy('uf_list')

##################################################
# Fim do Bloco [UF]
##################################################
