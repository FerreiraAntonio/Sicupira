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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('instituicao', views.InstituicaoList.as_view(), name='instituicao_list'),
    path('instituicao/view/<int:pk>', views.InstituicaoView.as_view(), name='instituicao_view'),
    path('instituicao/new', views.InstituicaoCreate.as_view(), name='instituicao_new'),
    path('instituicao/edit/<int:pk>', views.InstituicaoUpdate.as_view(), name='instituicao_edit'),
    path('instituicao/delete/<int:pk>', views.InstituicaoDelete.as_view(), name='instituicao_delete'),
]
