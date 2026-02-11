# forms.py
from django import forms
from .models import Indicacoes

class IndicacoesForm(forms.ModelForm):
    class Meta:
        model = Indicacoes
        fields = [
            "titulo",
            "descricao",
            "categoria",
            "urgencia",
            "logradouro",
            "numero_endereco",
            "bairro",
            "cep",
        ]
        widgets = {

            "titulo": forms.TextInput(attrs={
                "class": "border rounded p-2 w-full",
                "placeholder": "Título da Indicação"
            }),
            "descricao": forms.Textarea(attrs={
                "class": "border rounded p-2 w-full h-32",
                "placeholder": "Descrição detalhada da indicação"
            }),
            "categoria": forms.Select(attrs={"class": "border rounded p-2 w-full"}),
            "urgencia": forms.Select(attrs={"class": "border rounded p-2 w-full"}),
            "logradouro": forms.TextInput(attrs={
                "class": "border rounded p-2 w-full",
                "placeholder": "Rua / Logradouro"
            }),
            "numero_endereco": forms.TextInput(attrs={
                "class": "border rounded p-2 w-full",
                "placeholder": "Número"
            }),
            "bairro": forms.TextInput(attrs={
                "class": "border rounded p-2 w-full",
                "placeholder": "Bairro"
            }),
            "cep": forms.TextInput(attrs={
                "class": "border rounded p-2 w-full",
                "placeholder": "CEP"
            }),
        }
