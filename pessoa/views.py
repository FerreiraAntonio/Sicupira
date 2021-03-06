from django.contrib import messages
from django.core import serializers
from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.template.context_processors import csrf
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import *
from pessoa.models import Pessoa
from pessoa.models import Discente
from pessoa.models import Docente
from pessoa.models import Abreviatura
from sicupira.models import Programa, Curso

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from pessoa.services import LattesService


@login_required
def importaxml(request):
    if request.method == 'POST' and bool(request.FILES.get('myfile', False)):
        myfile = request.FILES['myfile']

        data = myfile.read()

        obj = LattesService.importXML(data)
        teste = obj.nome_pessoa

        request.session['pessoa_xml'] = obj
        return render(request, 'pessoa/discente.html', {
            'pessoaXML': obj,
            'obj': teste
        })


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

        if 'ano' in self.request.GET:
            programas = Programa.objects.filter(ano=self.request.GET['ano'])
            if programas.exists():
                programa_ids =[]
                for id in programas:
                    programa_ids.append(id)

                queryset = queryset.filter(curso__programa_id__in=programa_ids)
            else:
                queryset = queryset.filter(curso__programa_id=0)

        if 'nome' in self.request.GET:
            queryset = queryset.filter(pessoa__nome__icontains=self.request.GET['nome'])
        if 'instituicao' in self.request.GET:
            queryset = queryset.filter(curso__programa_id__instituicao__nome__icontains=self.request.GET['instituicao'])
        if 'programa' in self.request.GET:
            queryset = queryset.filter(curso__programa_id__nome_programa__icontains=self.request.GET['programa'])
        if 'situacao' in self.request.GET:
            queryset = queryset.filter(situacao__desc_situacao_matricula__icontains=self.request.GET['situacao'])
        if 'nivel' in self.request.GET:
            queryset = queryset.filter(nivel__desc_nivel_graduacao__icontains=self.request.GET['nivel'])

        return queryset


# @method_decorator(login_required(login_url='login'), name='dispatch')
# class DiscenteView(DetailView):
#     model = Discente

@login_required()
def discente_detail_view(request, id):
    discente = get_object_or_404(Discente, pk=id)
    abreviaturas = Abreviatura.objects.filter(pessoa_id= id)

    return render(request, 'pessoa/discente_detail.html', context={'discente': discente, 'abreviaturas':abreviaturas})

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

    # tramento para importar xml lates
    if request.method == 'POST' and "import_xml" in request.POST and bool(request.FILES.get('myfile', False)):
        myfile = request.FILES['myfile']

        if myfile.name.endswith('.xml'):
            data = myfile.read()
            pessoa_xml = LattesService.import_xml_memory(data)
            request.session["discente_pessoa_xml"] = pessoa_xml
        else:
            pessoa_xml = "Erro"

        return redirect("discente_new")

    dict_abrevs = []
    pessoa_xml = request.session.get("discente_pessoa_xml", None)
    if pessoa_xml:
        if pessoa_xml is not "Erro":
            messages.success(request, 'Currículo de(a), %s importado com sucesso.' % pessoa_xml["nome"])
            LattesService.fill_pessoa(pessoa, pessoa_xml, dict_abrevs)
            request.session["discente_pessoa_xml"] = None
        else:
            messages.success(request, 'Arquivo não é XML. Apenas arquivos XML podem ser importados!')
            request.session["discente_pessoa_xml"] = None

    # FIM tramento para importar xml lates

     # Preparação dos forms
    pessoa_form = PessoaForm(request.POST or None,instance=pessoa)
    discente_form = DiscenteForm(request.POST or None, instance=discente)
    AbreviaturaFormSet = inlineformset_factory(Pessoa, Abreviatura, form=AbreviaturaForm, extra=len(dict_abrevs)+1 )
    abreviatura_form = AbreviaturaFormSet(instance=pessoa)

    #inicializa o form com as abreviaturas do xml latters
    for subform, data in zip(abreviatura_form.forms, dict_abrevs):
        subform.initial = data

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

        return redirect('discente_list')

    args = {}
    args.update(csrf(request))
    args['pessoa_form'] = pessoa_form
    args['discente_form'] = discente_form
    args['abreviatura_form'] = abreviatura_form
    args['is_new'] = id <= 0

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
        if 'instituicao' in self.request.GET:
            queryset = queryset.filter(programa__instituicao__nome__icontains=self.request.GET['instituicao'])
        if 'programa' in self.request.GET:
            queryset = queryset.filter(programa__nome_programa__icontains=self.request.GET['programa'])
        if 'ano' in self.request.GET:
            queryset = queryset.filter(programa__ano__icontains=self.request.GET['ano'])
        if 'regime_trabalho' in self.request.GET:
            queryset = queryset.filter(regime_trabalho__desc_regime_trabalho__icontains=self.request.GET['regime_trabalho'])
        if 'categoria' in self.request.GET:
            queryset = queryset.filter(categoria__desc_categoria__icontains=self.request.GET['categoria'])

        return queryset


# @method_decorator(login_required(login_url='login'), name='dispatch')
# class DocenteView(DetailView):
#     model = Docente, Abreviatura

@login_required()
def docente_detail_view(request, id):
    docente = get_object_or_404(Docente, pk=id)
    abreviaturas = Abreviatura.objects.filter(pessoa_id= id)

    return render(request, 'pessoa/docente_detail.html', context={'docente': docente, 'abreviaturas':abreviaturas})

@method_decorator(login_required(login_url='login'), name='dispatch')
class DocenteCreate(CreateView):
    model = Docente
    fields = ['pessoa', 'titulo_nivel', 'data_titulacao', 'titulo_pais', 'regime_trabalho', 'vinculo_ies', 'programa', 'categoria']
    success_url = reverse_lazy('docente_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class DocenteUpdate(UpdateView):
    model = Docente
    fields = ['pessoa', 'titulo_nivel', 'data_titulacao', 'titulo_pais', 'regime_trabalho', 'vinculo_ies', 'programa', 'categoria']
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

    # tramento para importar xml lates
    dict_abrevs = []
    if request.method == 'POST' and "import_xml" in request.POST and bool(request.FILES.get('myfile', False)):
        myfile = request.FILES['myfile']

        if myfile.name.endswith('.xml'):
            data = myfile.read()
            pessoa_xml = LattesService.import_xml_memory(data)
            request.session["docente_pessoa_xml"] = pessoa_xml
        else:
            pessoa_xml = "Erro"

        return redirect("docente_new")

    pessoa_xml = request.session.get("docente_pessoa_xml", None)
    if pessoa_xml:
        if pessoa_xml is not "Erro":
            messages.success(request, 'Currículo de(a), %s importado com sucesso.' % pessoa_xml["nome"])
            LattesService.fill_pessoa(pessoa, pessoa_xml, dict_abrevs)
            request.session["docente_pessoa_xml"] = None
        else:
            messages.success(request, 'Arquivo não é XML. Apenas arquivos XML podem ser importados!')
            request.session["docente_pessoa_xml"] = None

    # FIM tramento para importar xml lates

    # Preparação dos forms
    pessoa_form = PessoaForm(request.POST or None,instance=pessoa)
    docente_form = DocenteForm(request.POST or None, instance=docente)
    AbreviaturaFormSet = inlineformset_factory(Pessoa, Abreviatura, form=AbreviaturaForm, extra=1)
    abreviatura_form = AbreviaturaFormSet(instance=pessoa)

    # inicializa o form com as abreviaturas do xml latters
    for subform, data in zip(abreviatura_form.forms, dict_abrevs):
        subform.initial = data

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
    args['is_new'] = id <= 0

    return render(request, template_name, args)

##################################################
# Fim do Bloco [Docente]
##################################################
