from django.forms import ModelForm
from .models import *


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class DiscenteForm(ModelForm):
    class Meta:
        model = Discente
        exclude = ['pessoa']


class DocenteForm(ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'


class AbreviaturaForm(ModelForm):
    class Meta:
        model = Abreviatura
        fields = '__all__'
