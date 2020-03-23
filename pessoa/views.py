from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import *

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from pessoa.services import LattesService

def importaxml2(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and bool(request.FILES.get('myfile', False)):
            myfile = request.FILES['myfile']
            data = myfile.read()
            #fs = FileSystemStorage()
            #filename = fs.save(myfile.name, myfile)
            #uploaded_file_url = fs.url(filename)

            obj = LattesService.importXML(data)
            teste = obj.nome
            return render(request, 'sicupira/importaxml.html', {
                'data': data,
                'obj': teste
            })
        return render(request, 'sicupira/importaxml.html', {})
    else:
        return redirect('login')

##################################################
# Inicio do Bloco [Discente]
# by Black Chan
##################################################
@method_decorator(login_required(login_url='login'), name='dispatch')
class DiscenteList(ListView):
    paginate_by = 10
    model = Discente

    def get_queryset(self):
        queryset = super(DiscenteList, self).get_queryset()
        queryset = queryset.order_by("nome_pessoa")

        if 'nome_pessoa' in self.request.GET:
            queryset = queryset.filter(nome_pessoa__icontains=self.request.GET['nome_pessoa'])
        if 'sexo_id' in self.request.GET:
            queryset = queryset.filter(sexo_id__desc_sexo__icontains=self.request.GET['sexo_id'])
        if 'data_nascimento' in self.request.GET:
            queryset = queryset.filter(data_nascimento__nome__icontains=self.request.GET['data_nascimento'])
        if 'numero_documento' in self.request.GET:
            queryset = queryset.filter(numero_documento__icontains=self.request.GET['numero_documento'])
        if 'tipo_documento_id' in self.request.GET:
            queryset = queryset.filter(
                tipo_documento_id__desc_tipo_doc__icontains=self.request.GET['tipo_documento_id'])
        if 'email' in self.request.GET:
            queryset = queryset.filter(email__icontains=self.request.GET['email'])
        if 'nacionalidade' in self.request.GET:
            queryset = queryset.filter(nacionalidade__nome_pais__icontains=self.request.GET['nacionalidade'])
        if 'titulo_nivel_id' in self.request.GET:
            queryset = queryset.filter(
                titulo_nivel_id__desc_nivel_graduacao__icontains=self.request.GET['titulo_nivel_id'])

        if 'curso_id' in self.request.GET:
            queryset = queryset.filter(curso_id__nome_curso__icontains=self.request.GET['curso_id'])
        if 'situacao_id' in self.request.GET:
            queryset = queryset.filter(situacao_id__desc_situacao_matricula__icontains=self.request.GET['situacao_id'])
        if 'data_situacao' in self.request.GET:
            queryset = queryset.filter(data_situacao__icontains=self.request.GET['data_situacao'])

        return queryset


@method_decorator(login_required(login_url='login'), name='dispatch')
class DiscenteView(DetailView):
    model = Discente


@method_decorator(login_required(login_url='login'), name='dispatch')
class DiscenteCreate(CreateView):
    model = Discente
    fields = ['nome_pessoa', 'sexo_id', 'data_nascimento', 'numero_documento', 'tipo_documento_id', 'email',
              'nacionalidade', 'titulo_nivel_id', 'curso_id', 'situacao_id', 'situacao_id', 'data_situacao']
    success_url = reverse_lazy('discente_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class DiscenteUpdate(UpdateView):
    model = Discente
    fields = ['nome_pessoa', 'sexo_id', 'data_nascimento', 'numero_documento', 'tipo_documento_id', 'email',
              'nacionalidade', 'titulo_nivel_id', 'curso_id', 'situacao_id', 'situacao_id', 'data_situacao']
    success_url = reverse_lazy('discente_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class DiscenteDelete(DeleteView):
    model = Discente
    success_url = reverse_lazy('discente_list')


##################################################
# Fim do Bloco [Discente]
##################################################


##################################################
# Inicio do Bloco [Docente]
# by Black Chan
##################################################
@method_decorator(login_required(login_url='login'), name='dispatch')
class DocenteList(ListView):
    paginate_by = 10
    model = Docente

    def get_queryset(self):
        queryset = super(DocenteList, self).get_queryset()
        queryset = queryset.order_by("nome_pessoa")

        if 'nome_pessoa' in self.request.GET:
            queryset = queryset.filter(nome_pessoa__icontains=self.request.GET['nome_pessoa'])
        if 'sexo_id' in self.request.GET:
            queryset = queryset.filter(sexo_id__desc_sexo__icontains=self.request.GET['sexo_id'])
        if 'data_nascimento' in self.request.GET:
            queryset = queryset.filter(data_nascimento__nome__icontains=self.request.GET['data_nascimento'])
        if 'numero_documento' in self.request.GET:
            queryset = queryset.filter(numero_documento__icontains=self.request.GET['numero_documento'])
        if 'tipo_documento_id' in self.request.GET:
            queryset = queryset.filter(
                tipo_documento_id__desc_tipo_doc__icontains=self.request.GET['tipo_documento_id'])
        if 'email' in self.request.GET:
            queryset = queryset.filter(email__icontains=self.request.GET['email'])
        if 'nacionalidade' in self.request.GET:
            queryset = queryset.filter(nacionalidade__nome_pais__icontains=self.request.GET['nacionalidade'])
        if 'titulo_nivel_id' in self.request.GET:
            queryset = queryset.filter(
                titulo_nivel_id__desc_nivel_graduacao__icontains=self.request.GET['titulo_nivel_id'])

        if 'data_titulacao' in self.request.GET:
            queryset = queryset.filter(data_titulacao__icontains=self.request.GET['data_titulacao'])
        if 'area_conhecimento' in self.request.GET:
            queryset = queryset.filter(area_conhecimento__icontains=self.request.GET['area_conhecimento'])
        if 'titulo_pais_id' in self.request.GET:
            queryset = queryset.filter(titulo_pais_id__nome_pais__icontains=self.request.GET['titulo_pais_id'])
        if 'regime_trabalho_id' in self.request.GET:
            queryset = queryset.filter(
                regime_trabalho_id__desc_regime_trabalho__icontains=self.request.GET['regime_trabalho_id'])
        if 'vinculo_IES' in self.request.GET:
            queryset = queryset.filter(vinculo_IES__desc_vinclulo_ies__icontains=self.request.GET['vinculo_IES'])

        return queryset


@method_decorator(login_required(login_url='login'), name='dispatch')
class DocenteView(DetailView):
    model = Docente


@method_decorator(login_required(login_url='login'), name='dispatch')
class DocenteCreate(CreateView):
    model = Docente
    fields = ['nome_pessoa', 'sexo_id', 'data_nascimento', 'numero_documento', 'tipo_documento_id', 'email',
              'nacionalidade', 'titulo_nivel_id', 'data_titulacao', 'area_conhecimento', 'titulo_pais_id',
              'regime_trabalho_id', 'vinculo_IES']
    success_url = reverse_lazy('docente_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class DocenteUpdate(UpdateView):
    model = Docente
    fields = ['nome_pessoa', 'sexo_id', 'data_nascimento', 'numero_documento', 'tipo_documento_id', 'email',
              'nacionalidade', 'titulo_nivel_id', 'data_titulacao', 'area_conhecimento', 'titulo_pais_id',
              'regime_trabalho_id', 'vinculo_IES']
    success_url = reverse_lazy('docente_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class DocenteDelete(DeleteView):
    model = Docente
    success_url = reverse_lazy('docente_list')


##################################################
# Fim do Bloco [Docente]
##################################################
