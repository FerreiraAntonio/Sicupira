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
    path('instituicao', views.InstituicaoList.as_view(), name='instituicao_list'),
    path('instituicao/view/<int:pk>', views.InstituicaoView.as_view(), name='instituicao_view'),
    path('instituicao/new', views.InstituicaoCreate.as_view(), name='instituicao_new'),
    path('instituicao/edit/<int:pk>', views.InstituicaoUpdate.as_view(), name='instituicao_edit'),
    path('instituicao/delete/<int:pk>', views.InstituicaoDelete.as_view(), name='instituicao_delete'),
    path('uf', views.UFList.as_view(), name='uf_list'),
    path('uf/view/<int:pk>', views.UFView.as_view(), name='uf_view'),
    path('uf/new', views.UFCreate.as_view(), name='uf_new'),
    path('uf/edit/<int:pk>', views.UFUpdate.as_view(), name='uf_edit'),
    path('uf/delete/<int:pk>', views.UFDelete.as_view(), name='uf_delete'),
]
