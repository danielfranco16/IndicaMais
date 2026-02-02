# Indica+  

Sistema web integrado para a gestão e acompanhamento de **indicações legislativas**, visando melhorar a comunicação entre a população, o Legislativo e o Executivo municipal.  

O Indica+ foi desenvolvido com foco em **transparência, organização e acessibilidade**, permitindo que cidadãos acompanhem suas demandas e que servidores e vereadores gerenciem as indicações legislativas de forma eficiente.  


## 🔹 Módulos do Sistema

| Módulo | Perfil de Usuário | Autenticação | Tela Inicial | Funcionalidades |
|--------|-----------------|--------------|-------------|----------------|
| Demandas | Usuário Cidadão | Não necessário | Landing Page | Visualização e envio de indicações |
| Indicações | Usuário Vereador | Login requerido | Dashboard Vereador | Gerenciamento das indicações recebidas e enviadas |
| Legislativo | Usuário Servidor da Câmara | Login requerido | Dashboard Câmara | Controle e acompanhamento das demandas legislativas |
| Executivo | Usuário Servidor da Prefeitura | Login requerido | Dashboard Prefeitura | Recebimento, análise e resposta das indicações enviadas |

---

## 💻 Tecnologias Utilizadas

O desenvolvimento da solução foi realizado utilizando:

- **Python 3.11** – Linguagem de programação do back-end  
- **Django 5.2.10** – Framework web baseado na arquitetura MVT  
- **PostgreSQL 17.7** – Banco de dados relacional  
- **HTML5 / CSS3 / JavaScript (ES6+)** – Estruturação e interatividade do front-end  
- **Tailwind CSS 3.3** – Framework CSS utilitário para design responsivo  
- **VS Code 1.10.2008** – IDE para desenvolvimento  
- **Git 2.42** – Controle de versão  
- **Navegadores** – Safari / Firefox para testes e execução  
- **Stitch (online)** – Ferramenta de prototipagem de interfaces baseada em IA  

---

## 📦 Dependências Python

| Pacote | Versão | Observações |
|--------|--------|-------------|
| altgraph | 0.17.2 | Biblioteca auxiliar para análise de dependências |
| future | 0.18.2 | Compatibilidade entre versões do Python |
| macholib | 1.15.2 | Manipulação de binários em macOS |
| six | 1.15.0 | Compatibilidade Python 2 e 3 |
| asgiref | 3.11.0 | Interface ASGI para suporte a apps assíncronas |
| Django | 5.2.10 | Framework web MVT |
| django-extensions | 4.1 | Extensões adicionais para produtividade |
| pip | 25.3 | Gerenciador de pacotes Python |
| setuptools | 65.5.0 | Ferramenta para empacotamento de bibliotecas |
| sqlparse | 0.5.5 | Análise e formatação de consultas SQL |

---

## ⚙ Dependências Django

| Aplicativo | Versão | Observações |
|------------|--------|-------------|
| django.contrib.admin | 5.2.10 | Interface administrativa padrão |
| django.contrib.auth | 5.2.10 | Sistema de autenticação e autorização |
| django.contrib.contenttypes | 5.2.10 | Gerenciamento de tipos de conteúdo |
| django.contrib.sessions | 5.2.10 | Gerenciamento de sessões de usuários |
| django.contrib.messages | 5.2.10 | Sistema de mensagens temporárias |
| django.contrib.staticfiles | 5.2.10 | Gerenciamento de arquivos estáticos |
| django_extensions | 4.1 | Comandos e utilitários adicionais |

---

## 🚀 Instalação e Execução do Projeto

Siga os passos abaixo para rodar o Indica+ localmente:  

## Clonar o repositório

git clone https://github.com/danielfranco16/IndicaMais.git


## 🐍 Criar e ativar um ambiente virtual

python -m venv venv

## 💻 No Windows
venv\Scripts\activate
## 🖥️ No macOS / Linux
source venv/bin/activate

## 📦 Instalar dependências
pip install -r requirements.txt

### 🗄️ Configurar Banco de Dados 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'indica_mais_db',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



## 🔄 Executar Migrações 
python manage.py makemigrations
python manage.py migrate


## 👤 Criar Usuário ADM Django 
python manage.py createsuperuser

## ▶️ Executar Servidor Local 
python manage.py runserver


## 📝 Local 

MIT License © Daniel Messias Franco dos Santos









