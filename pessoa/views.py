from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.template.context_processors import csrf
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#from .models import *
from .forms import *
from pessoa.models import Pessoa
from pessoa.models import Discente
from pessoa.models import Docente
from pessoa.models import Vinculo
from pessoa.models import Orienta
from pessoa.models import Abreviatura

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from pessoa.services import LattesService


@login_required
def importaxml2(request):
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
        queryset = queryset.order_by("pessoa__nome")

        if 'nome' in self.request.GET:
            queryset = queryset.filter(pessoa__nome__icontains=self.request.GET['nome'])
        if 'sexo' in self.request.GET:
            queryset = queryset.filter(pessoa__sexo__desc_sexo__icontains=self.request.GET['sexo'])
        if 'data_nascimento' in self.request.GET:
            queryset = queryset.filter(pessoa__data_nascimento__icontains=self.request.GET['data_nascimento'])
        if 'numero_documento' in self.request.GET:
            queryset = queryset.filter(pessoa__numero_documento__icontains=self.request.GET['numero_documento'])
        if 'tipo_documento' in self.request.GET:
            queryset = queryset.filter(pessoa__tipo_documento__desc_tipo_doc__icontains=self.request.GET['tipo_documento'])
        if 'email' in self.request.GET:
            queryset = queryset.filter(pessoa__email__icontains=self.request.GET['email'])
        if 'nacionalidade' in self.request.GET:
            queryset = queryset.filter(pessoa__nacionalidade__nome_pais__icontains=self.request.GET['nacionalidade'])
        if 'curso' in self.request.GET:
            queryset = queryset.filter(curso__nome_curso__icontains=self.request.GET['curso'])
        if 'situacao' in self.request.GET:
            queryset = queryset.filter(situacao__desc_situacao_matricula__icontains=self.request.GET['situacao'])
        if 'data_situacao' in self.request.GET:
            queryset = queryset.filter(data_situacao__icontains=self.request.GET['data_situacao'])
        if 'nivel' in self.request.GET:
            queryset = queryset.filter(nivel__desc_nivel_graduacao__icontains=self.request.GET['nivel'])

        return queryset


@method_decorator(login_required(login_url='login'), name='dispatch')
class DiscenteView(DetailView):
    model = Discente


@method_decorator(login_required(login_url='login'), name='dispatch')
class DiscenteCreate(CreateView):
    model = Discente
    fields = ['pessoa', 'nivel', 'curso', 'situacao', 'data_situacao']
    success_url = reverse_lazy('discente_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class DiscenteUpdate(UpdateView):
    model = Discente
    fields = ['pessoa', 'nivel', 'curso', 'situacao', 'data_situacao']
    success_url = reverse_lazy('discente_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class DiscenteDelete(DeleteView):
    model = Discente
    success_url = reverse_lazy('discente_list')

@login_required
def save_discente(request, id=0, template_name='pessoa/discente_form.html'):
    if id > 0:
        discente = get_object_or_404(Discente, pk=id)
        pessoa = discente.pessoa
    else:
        discente = Discente()
        pessoa = Pessoa()

    # Preparação dos forms
    pessoa_form = PessoaForm(request.POST or None,instance=pessoa)
    discente_form = DiscenteForm(request.POST or None, instance=discente)
    AbreviaturaFormSet = inlineformset_factory(Pessoa, Abreviatura, form=AbreviaturaForm, extra=1)
    abreviatura_form = AbreviaturaFormSet(instance=pessoa)

    if request.method == 'POST' and pessoa_form.is_valid() and discente_form.is_valid():
        # transação
        with transaction.atomic():

            pessoa = pessoa_form.save()
            discente = discente_form.save(False)

            discente.pessoa = pessoa
            discente.save()

            abreviatura_form = AbreviaturaFormSet(request.POST, instance=pessoa)
            print(abreviatura_form.is_valid())
            if abreviatura_form.is_valid():
                abreviatura_form.save()

        #return render(request, "pessoa/discente_list.html")
        return redirect('discente_list')

    args = {}
    args.update(csrf(request))
    args['pessoa_form'] = pessoa_form
    args['discente_form'] = discente_form
    args['abreviatura_form'] = abreviatura_form

    return render(request, template_name, args)

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
        queryset = queryset.order_by("pessoa__nome")

        if 'nome' in self.request.GET:
            queryset = queryset.filter(pessoa__nome__icontains=self.request.GET['nome'])
        if 'sexo' in self.request.GET:
            queryset = queryset.filter(pessoa__sexo__desc_sexo__icontains=self.request.GET['sexo'])
        if 'data_nascimento' in self.request.GET:
            queryset = queryset.filter(pessoa__data_nascimento__icontains=self.request.GET['data_nascimento'])
        if 'numero_documento' in self.request.GET:
            queryset = queryset.filter(pessoa__numero_documento__icontains=self.request.GET['numero_documento'])
        if 'tipo_documento' in self.request.GET:
            queryset = queryset.filter(pessoa__tipo_documento__desc_tipo_doc__icontains=self.request.GET['tipo_documento'])
        if 'email' in self.request.GET:
            queryset = queryset.filter(pessoa__email__icontains=self.request.GET['email'])
        if 'nacionalidade' in self.request.GET:
            queryset = queryset.filter(pessoa__nacionalidade__nome_pais__icontains=self.request.GET['nacionalidade'])
        if 'titulo_nivel' in self.request.GET:
            queryset = queryset.filter(titulo_nivel__desc_nivel_graduacao__icontains=self.request.GET['titulo_nivel'])
        if 'data_titulacao' in self.request.GET:
            queryset = queryset.filter(data_titulacao__icontains=self.request.GET['data_titulacao'])
        if 'area_conhecimento' in self.request.GET:
            queryset = queryset.filter(area_conhecimento__icontains=self.request.GET['area_conhecimento'])
        if 'titulo_pais' in self.request.GET:
            queryset = queryset.filter(titulo_pais__nome_pais__icontains=self.request.GET['titulo_pais'])
        if 'regime_trabalho' in self.request.GET:
            queryset = queryset.filter(regime_trabalho__desc_regime_trabalho__icontains=self.request.GET['regime_trabalho'])
        if 'vinculo_ies' in self.request.GET:
            queryset = queryset.filter(vinculo_ies__desc_vinculo_ies__icontains=self.request.GET['vinculo_ies'])

        return queryset


@method_decorator(login_required(login_url='login'), name='dispatch')
class DocenteView(DetailView):
    model = Docente


@method_decorator(login_required(login_url='login'), name='dispatch')
class DocenteCreate(CreateView):
    model = Docente
    fields = ['pessoa', 'titulo_nivel', 'data_titulacao', 'titulo_pais', 'regime_trabalho', 'vinculo_ies']
    success_url = reverse_lazy('docente_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class DocenteUpdate(UpdateView):
    model = Docente
    fields = ['pessoa', 'titulo_nivel', 'data_titulacao', 'titulo_pais', 'regime_trabalho', 'vinculo_ies']
    success_url = reverse_lazy('docente_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class DocenteDelete(DeleteView):
    model = Docente
    success_url = reverse_lazy('docente_list')

@login_required
def save_docente(request, id=0, template_name='pessoa/docente_form.html'):
    if id > 0:
        docente = get_object_or_404(Docente, pk=id)
        pessoa = docente.pessoa
    else:
        docente = Docente()
        pessoa = Pessoa()

    # Preparação dos forms
    pessoa_form = PessoaForm(request.POST or None,instance=pessoa)
    docente_form = DocenteForm(request.POST or None, instance=docente)
    AbreviaturaFormSet = inlineformset_factory(Pessoa, Abreviatura, form=AbreviaturaForm, extra=1)
    abreviatura_form = AbreviaturaFormSet(instance=pessoa)

    if request.method == 'POST' and pessoa_form.is_valid() and docente_form.is_valid():
        # transação
        with transaction.atomic():

            pessoa = pessoa_form.save()
            docente = docente_form.save(False)

            docente.pessoa = pessoa
            docente.save()

            abreviatura_form = AbreviaturaFormSet(request.POST, instance=pessoa)
            print(abreviatura_form.is_valid())
            if abreviatura_form.is_valid():
                abreviatura_form.save()

        return redirect('docente_list')

    args = {}
    args.update(csrf(request))
    args['pessoa_form'] = pessoa_form
    args['docente_form'] = docente_form
    args['abreviatura_form'] = abreviatura_form

    return render(request, template_name, args)

##################################################
# Fim do Bloco [Docente]
##################################################
