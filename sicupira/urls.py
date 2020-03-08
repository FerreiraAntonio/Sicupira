"""webserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

################################################
# CADA NOVA VIEW DEVE SER INSERIDA ABAIXO
# SEGUINDO OS PADRÕES DAS ANTERIORES E DE ACORDO
# COM OS NOMES DEFINIDOS PARA AS VIEWS CRIADAS
################################################

urlpatterns = [
    path('index', views.index, name='index'),
    path('importaxml', views.importaxml, name='importaxml'),
    path('programa', views.ProgramaList.as_view(), name='programa_list'),
    path('programa/view/<int:pk>', views.ProgramaView.as_view(), name='programa_view'),
    path('programa/new', views.ProgramaCreate.as_view(), name='programa_new'),
    path('programa/edit/<int:pk>', views.ProgramaUpdate.as_view(), name='programa_edit'),
    path('programa/delete/<int:pk>', views.ProgramaDelete.as_view(), name='programa_delete'),
    path('enderecoprograma', views.EnderecoProgramaList.as_view(), name='enderecoprograma_list'),
    path('enderecoprograma/view/<int:pk>', views.EnderecoProgramaView.as_view(), name='enderecoprograma_view'),
    path('enderecoprograma/new', views.EnderecoProgramaCreate.as_view(), name='enderecoprograma_new'),
    path('enderecoprograma/edit/<int:pk>', views.EnderecoProgramaUpdate.as_view(), name='enderecoprograma_edit'),
    path('enderecoprograma/delete/<int:pk>', views.EnderecoProgramaDelete.as_view(), name='enderecoprograma_delete'),
    path('turma', views.TurmaList.as_view(), name='turma_list'),
    path('turma/view/<int:pk>', views.TurmaView.as_view(), name='turma_view'),
    path('turma/new', views.TurmaCreate.as_view(), name='turma_new'),
    path('turma/edit/<int:pk>', views.TurmaUpdate.as_view(), name='turma_edit'),
    path('turma/delete/<int:pk>', views.TurmaDelete.as_view(), name='turma_delete'),
    path('estado', views.EstadoList.as_view(), name='estado_list'),
    path('estado/view/<int:pk>', views.EstadoView.as_view(), name='estado_view'),
    path('estado/new', views.EstadoCreate.as_view(), name='estado_new'),
    path('estado/edit/<int:pk>', views.EstadoUpdate.as_view(), name='estado_edit'),
    path('estado/delete/<int:pk>', views.EstadoDelete.as_view(), name='estado_delete'),
    path('linhapesquisa', views.LinhaPesquisaList.as_view(), name='linhapesquisa_list'),
    path('linhapesquisa/view/<int:pk>', views.LinhaPesquisaView.as_view(), name='linhapesquisa_view'),
    path('linhapesquisa/new', views.LinhaPesquisaCreate.as_view(), name='linhapesquisa_new'),
    path('linhapesquisa/edit/<int:pk>', views.LinhaPesquisaUpdate.as_view(), name='linhapesquisa_edit'),
    path('linhapesquisa/delete/<int:pk>', views.LinhaPesquisaDelete.as_view(), name='linhapesquisa_delete'),
    path('disciplina', views.DisciplinaList.as_view(), name='disciplina_list'),
    path('disciplina/view/<int:pk>', views.DisciplinaView.as_view(), name='disciplina_view'),
    path('disciplina/new', views.DisciplinaCreate.as_view(), name='disciplina_new'),
    path('disciplina/edit/<int:pk>', views.DisciplinaUpdate.as_view(), name='disciplina_edit'),
    path('disciplina/delete/<int:pk>', views.DisciplinaDelete.as_view(), name='disciplina_delete'),
]
