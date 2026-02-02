import random
from django.db import models
from datetime import datetime


class Demanda(models.Model):
    # Opções para garantir padronização no banco de dados
    STATUS_CHOICES = [
        ("cadastrada", "Cadastrada"),
        ("em_analise", "Em Análise"),
        ("em_execucao", "Em Execução"),
        ("concluido", "Concluído"),
        ("cancelado", "Cancelado"),
    ]

    URGENCIA_CHOICES = [
        ("baixa", "Baixa"),
        ("media", "Média"),
        ("alta", "Alta"),
        ("critica", "Crítica"),
    ]

    CATEGORIA_CHOICES = [
        ("pavimentacao", "Pavimentação e Tapa-buracos"),
        ("iluminacao", "Iluminação Pública"),
        ("saneamento", "Saneamento e Drenagem"),
        ("limpeza", "Limpeza Urbana e Resíduos"),
        ("arborizacao", "Poda de Árvores e Jardins"),
        ("sinalizacao", "Trânsito e Sinalização"),
        ("zoonoses", "Zoonoses e Animais"),
        ("fiscalizacao", "Fiscalização de Obras/Posturas"),
        ("equipamentos", "Equipamentos Públicos (Parques/Praças)"),
        ("outros", "Outros Assuntos"),
    ]

    # --- Identificação ---
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descricao = models.TextField(verbose_name="Descrição")
    protocolo = models.CharField(max_length=30, unique=True, verbose_name="Protocolo")

    # --- Classificação ---
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Cadastrada",
        verbose_name="Situação",
    )

    urgencia = models.CharField(
        max_length=20,
        choices=URGENCIA_CHOICES,
        default="baixa",
        verbose_name="Nível de Urgência",
    )
    # Sugestão: Se houver muitas categorias fixas, considere criar um Model separado para 'Categoria'

    # Atualizando o campo na classe Model:
    categoria = models.CharField(
        max_length=50,
        choices=CATEGORIA_CHOICES,
        default="outros",
        verbose_name="Categoria",
    )

    # --- Datas (Timestamps) ---
    # auto_now_add=True preenche automaticamente na criação
    data_cadastro = models.DateTimeField(
        auto_now_add=True, verbose_name="Data de Cadastro"
    )
    # auto_now=True atualiza sempre que o objeto for salvo
    data_atualizacao = models.DateTimeField(
        auto_now=True, verbose_name="Última Atualização"
    )
    # null=True e blank=True permitem que o campo fique vazio até a conclusão
    data_conclusao = models.DateTimeField(
        null=True, blank=True, verbose_name="Data de Conclusão"
    )

    # --- Localização ---
    logradouro = models.CharField(max_length=255, verbose_name="Logradouro")
    numero_endereco = models.CharField(max_length=20, verbose_name="Número")
    bairro = models.CharField(max_length=100, verbose_name="Bairro")
    cep = models.CharField(max_length=10, verbose_name="CEP")

    # --- Solicitante ---
    nome_autor = models.CharField(max_length=150, verbose_name="Nome do Solicitante")
    email_autor = models.EmailField(verbose_name="Contato do Solicitante")
    telefone_autor = models.CharField(max_length=20, verbose_name="Telefone do Solicitante")

class Meta:
    verbose_name = "Demanda"
    verbose_name_plural = "Demandas"
    ordering = ["-data_cadastro"]  # Ordena do mais recente para o mais antigo

def __str__(self):
    return f"{self.protocolo} - {self.titulo}"

def gerar_protocolo(nome_autor):
    ano = str(datetime.now().year)[-2:]
    mes = str(datetime.now().month)[-1] 
    dia = str(datetime.now().day)[0]

  
    nome_limpo = nome_autor.strip().upper()
    if nome_limpo:
        primeira = nome_limpo[0]
        ultima = nome_limpo[-1]
        letras = f"{primeira}{ultima}"
    else:
        letras = "XX"

        # Loop para garantir que não repita
    while True:
        codigo = random.randint(1000, 9999)
        protocolo_final = f"{ano}{mes}{dia}-{codigo}-{letras}"
            # Verifica no banco se já existe
        if not Demanda.objects.filter(protocolo=protocolo_final).exists():
            return protocolo_final
