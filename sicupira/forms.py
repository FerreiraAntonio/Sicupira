from django.forms import ModelForm
from sicupira.models import EnderecoPrograma
from sicupira.models import TelefoneEnderecoPrograma


class EnderecoProgramaForm(ModelForm):
    class Meta:
        model = EnderecoPrograma
        fields = '__all__'


class TelefoneEnderecoProgramaForm(ModelForm):
    class Meta:
        model = TelefoneEnderecoPrograma
        fields = '__all__'
