

### Passo 1: Instalar o Python
Certifique-se de que o Python está instalado no seu sistema. 

python --version



### Passo 2: Criar um Ambiente Virtual
""" Um ambiente virtual é recomendado para isolar as dependências do seu projeto. 
Crie e ative um ambiente virtual com os comandos:"""


# Criar o ambiente virtual
python -m venv env

# Ativar o ambiente virtual (Windows)
env\Scripts\activate



### Passo 3: Instalar o Django -- 

"""Com o ambiente virtual ativado, instale o Django rodando:"""

pip install django


### Passo 4: Criar um Projeto Django
"""Após instalar o Django, crie um projeto com o comando `django-admin startproject`:"""


django-admin startproject core .


Isso criará uma estrutura básica de diretórios para o projeto.

### Passo 5: Criar um Aplicativo Django
Dentro do projeto, crie um novo aplicativo (app) com o comando:


python manage.py startapp financas


Isso criará uma nova pasta com a estrutura básica do app. Lembre-se de registrar o app no arquivo `settings.py`, na seção `INSTALLED_APPS`.

### Passo 6: Estrutura do Projeto
Dentro da pasta do projeto, a estrutura:


controle-financas/
│
├── env/                # Pasta do ambiente virtual
│   ├── bin/            # Executáveis do ambiente virtual (no Windows: Scripts/)
│   ├── lib/            # Pacotes Python instalados no ambiente virtual. Cada dependência instalada via pip será salva aqui.
│   └── ...             # Outros arquivos e pastas do ambiente virtual, incluindo arquivos de configuração e cache.
│
├── manage.py           # Arquivo de gerenciamento do Django.
│                       # Usado para rodar o servidor, executar migrações, criar usuários, etc.
│
├── core/               # Diretório principal do projeto Django, contendo configurações e arquivos essenciais.
│   ├── __init__.py     # Torna o diretório `core` um pacote Python, permitindo que ele seja importado como módulo.
│   ├── settings.py     # Arquivo de configuração principal do Django. Define parâmetros como banco de dados, apps instalados, segurança e mais.
│   ├── urls.py         # Define o roteamento das URLs do projeto. Conecta URLs às views responsáveis por processar as requisições.
│   ├── asgi.py         # Configuração da interface ASGI, usada para comunicação assíncrona no Django.
│   └── wsgi.py         # Configuração da interface WSGI, usada para a comunicação síncrona entre o servidor web e o Django.
│
└── financas/           # Aplicativo Django chamado "financas", responsável por funcionalidades específicas do projeto.
    ├── __init__.py     # Torna o diretório `financas` um pacote Python, assim como no diretório `core`.
    ├── admin.py        # Arquivo para configurar a administração do Django (Django Admin). Você pode registrar modelos para gerenciá-los no admin.
    ├── apps.py         # Arquivo de configuração do app `financas`. Contém informações como nome e comportamento do app.
    ├── models.py       # Arquivo onde você define os modelos de dados (tabelas do banco de dados). Cada modelo será mapeado para uma tabela.
    ├── tests.py        # Define os testes unitários e de integração para o app `financas`. Usado para garantir que tudo funciona como esperado.
    └── views.py        # Define as views do app `financas`, que são funções ou classes que processam requisições HTTP e retornam respostas (páginas, etc.).


### Passo 7: Rodar o Servidor de Desenvolvimento
"""Agora, você pode iniciar o servidor de desenvolvimento para testar o projeto:"""

python manage.py runserver


"""O Django irá rodar o servidor na URL `http://127.0.0.1:8000/`."""



### Passo 8: Configurar o Banco de Dados
No arquivo `settings.py`, configure o banco de dados. Por padrão, o Django usa SQLite, mas você pode configurar PostgreSQL, MySQL ou outro banco.

## Neste caso iremos usar a configuracao por padrao o SQLite

### Passo 9: Aplicar as Migrações
O Django cria tabelas no banco de dados baseado nos modelos definidos nos apps. Para aplicar as migrações iniciais:


python manage.py migrate


### Passo 10: Criar um Superusuário
Para acessar o painel administrativo do Django, crie um superusuário:


python manage.py createsuperuserv


Siga as instruções para criar nome de usuário e senha.

### Passo 11: Testar o Painel Administrativo
Agora você pode acessar o painel administrativo do Django visitando `http://127.0.0.1:8000/admin/` e utilizando o superusuário que acabou de criar.

# Final correr o comando

python manage.py runserver

git config --global user.name "Ezequias S. Santos"
git config --global user.email "phd.esantos@gmail.com"




### Passo 12: Criar Modelos e Visualizações
Dentro do seu app, edite o arquivo `models.py` para criar os modelos da aplicação, e o arquivo `views.py` para definir as visualizações que irão processar as requisições. 

Após definir os modelos, rode as migrações novamente:

python manage.py makemigrations
python manage.py migrate


### Passo 13: Criar Rotas
No arquivo `urls.py` do seu app ou projeto, defina as rotas (URLs) que irão apontar para as visualizações.

### Passo 14: Testar e Desenvolver
Continue desenvolvendo o seu projeto adicionando novas funcionalidades, criando templates, e ajustando as configurações conforme necessário.

### Dica: Usar Docker (Opcional)
Para facilitar o ambiente de desenvolvimento, você pode usar o Docker para isolar o projeto completamente. Isso inclui configurar serviços como banco de dados e o próprio Django em contêineres.

Esse é o fluxo básico para criar um projeto Django!