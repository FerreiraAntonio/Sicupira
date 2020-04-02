from django.forms import ModelForm
from sicupira.models import EnderecoPrograma
from sicupira.models import TelefoneEnderecoPrograma
from sicupira.models import LinhaPesquisa
from django import forms

class EnderecoProgramaForm(ModelForm):
    class Meta:
        model = EnderecoPrograma
        fields = '__all__'


class TelefoneEnderecoProgramaForm(ModelForm):
    class Meta:
        model = TelefoneEnderecoPrograma
        fields = '__all__'


class LinhaPesquisaForm(ModelForm):
    class Meta:
        model = LinhaPesquisa
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        data_inicio = cleaned_data.get("data_inicio")
        data_fim = cleaned_data.get("data_fim")
        if data_inicio > data_fim:
            msg = "Data inicio deve ser menor que data fim."
            raise forms.ValidationError(msg)
