#forms.py
from django import forms
from .models import Cliente, Entrega
from localflavor.br.forms import BRCPFField, BRCNPJField, BRZipCodeField

class ClienteForm(forms.ModelForm):
    # Campos com validação brasileira e placeholders para o usuário
    cpf = BRCPFField(label="CPF", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}))
    cnpj = BRCNPJField(label="CNPJ", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00.000.000/0000-00'}))
    cep = BRZipCodeField(label="CEP", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00000-000'}))

    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'cnpj', 'cep', 'endereco', 'numero', 'bairro', 'cidade', 'uf', 'celular', 'email']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '2'}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(00) 00000-0000'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = ['remetente', 'destinatario', 'descricao_carga', 'peso', 'valor_frete']
        widgets = {
            'remetente': forms.Select(attrs={'class': 'form-control'}),
            'destinatario': forms.Select(attrs={'class': 'form-control'}),
            'descricao_carga': forms.TextInput(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_frete': forms.NumberInput(attrs={'class': 'form-control'}),
        }