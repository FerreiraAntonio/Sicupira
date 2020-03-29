from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django.contrib.admin.helpers import Fieldset
from django.forms import ModelForm, inlineformset_factory, forms
from .models import *


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

class DiscenteForm(ModelForm):
    class Meta:
        model = Discente
        fields = '__all__'


class DocenteForm(ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'

class AbreviaturaForm(ModelForm):

    class Meta:
        model = Abreviatura
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AbreviaturaForm, self).__init__(*args, **kwargs)
        print(self.fields)
        #new_choices = [('Sim', 'Não')]
        #self.fields['flg_principal'].extend(new_choices)




