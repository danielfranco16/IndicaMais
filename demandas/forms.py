from django import forms
from .models import Demanda

class DemandaForm(forms.ModelForm):
    class Meta:
        model = Demanda
        # Definimos apenas os campos que o usuário deve preencher
        fields = [
            'nome_autor', 'email_autor', 'telefone_autor',
            'titulo', 'descricao', 'categoria', 'urgencia',
            'cep', 'logradouro', 'numero_endereco', 'bairro'
        ]

        # Estilos CSS (Tailwind) reutilizados para manter o padrão visual
        STYLE_INPUT = "form-input flex w-full rounded-lg text-[#111318] dark:text-white focus:outline-0 focus:ring-2 focus:ring-primary/50 border border-[#dbdfe6] dark:border-[#4A5568] bg-white dark:bg-[#2D3748] h-12 placeholder:text-[#9ca3af] px-4 text-base font-normal transition-all"
        STYLE_SELECT = "form-select flex w-full rounded-lg text-[#111318] dark:text-white focus:outline-0 focus:ring-2 focus:ring-primary/50 border border-[#dbdfe6] dark:border-[#4A5568] bg-white dark:bg-[#2D3748] h-12 px-4 text-base font-normal transition-all"
        STYLE_TEXTAREA = "form-textarea flex w-full min-h-[140px] resize-y rounded-lg text-[#111318] dark:text-white focus:outline-0 focus:ring-2 focus:ring-primary/50 border border-[#dbdfe6] dark:border-[#4A5568] bg-white dark:bg-[#2D3748] placeholder:text-[#9ca3af] p-4 text-base font-normal transition-all"

        widgets = {
            # --- Solicitante ---
            'nome_autor': forms.TextInput(attrs={'class': STYLE_INPUT, 'placeholder': 'Seu nome completo'}),
            'email_autor': forms.EmailInput(attrs={'class': STYLE_INPUT, 'placeholder': 'seu@email.com'}),
            'telefone_autor': forms.TextInput(attrs={'class': STYLE_INPUT, 'placeholder': '(00) 00000-0000', 'data-mask': '(00) 00000-0000'}),

            # --- Identificação da Demanda ---
            'titulo': forms.TextInput(attrs={'class': STYLE_INPUT, 'placeholder': 'Resumo do problema (ex: Buraco na rua X)'}),
            'descricao': forms.Textarea(attrs={'class': STYLE_TEXTAREA, 'placeholder': 'Descreva detalhadamente a situação, pontos de referência, etc.'}),
            'categoria': forms.Select(attrs={'class': STYLE_SELECT}),
            'urgencia': forms.Select(attrs={'class': STYLE_SELECT}),

            # --- Localização ---
            'cep': forms.TextInput(attrs={'class': STYLE_INPUT, 'placeholder': '00000-000', 'id': 'cep'}), # ID para script de busca de CEP
            'logradouro': forms.TextInput(attrs={'class': STYLE_INPUT, 'placeholder': 'Rua, Avenida, Travessa...'}),
            'numero_endereco': forms.TextInput(attrs={'class': STYLE_INPUT, 'placeholder': 'Nº ou S/N'}),
            'bairro': forms.TextInput(attrs={'class': STYLE_INPUT, 'placeholder': 'Nome do Bairro'}),
        }