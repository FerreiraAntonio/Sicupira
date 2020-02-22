from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from sicupira.models import Instituicao, UF


def index(request):
    return render(request, 'sicupira/index.html', {})

##################################################
# ATENÇÃO: CADA DESENVOLVEDOR DEVE DUPLICAR      #
# UM BLOCO PARA CADA CLASSE. PARA ISSO BASTA     #
# COPIAR, COLAR E DEPOIS RENOMEAR A CLASSE PARA  #
# O NOME DA NOVA CLASSE.                         #
##################################################


##################################################
# Inicio do Bloco [Instituicao]
# by Antonio Horta
##################################################


class InstituicaoList(ListView):
    model = Instituicao


class InstituicaoView(DetailView):
    model = Instituicao


class InstituicaoCreate(CreateView):
    model = Instituicao
    fields = ['nome', 'uf', 'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'municipio', 'fax', 'telefone', 'ramal', 'email', 'url', 'inicio', 'fim', 'latitude', 'longitude']
    success_url = reverse_lazy('instituicao_list')


class InstituicaoUpdate(UpdateView):
    model = Instituicao
    fields = ['nome', 'uf', 'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'municipio', 'fax', 'telefone', 'ramal', 'email', 'url', 'inicio', 'fim', 'latitude', 'longitude']
    success_url = reverse_lazy('instituicao_list')


class InstituicaoDelete(DeleteView):
    model = Instituicao
    success_url = reverse_lazy('instituicao_list')

##################################################
# Fim do Bloco [Instituicao]
##################################################

##################################################
# Inicio do Bloco [UF]
# by Antonio Horta
##################################################


class UFList(ListView):
    model = UF


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
