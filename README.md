# E-commerce

- **Para fazer passo a passo, verifique a pasta `BKP`.**

Projeto simples de e-commerce feito com Python e Django. O e-commerce contém páginas de produtos, carrinho e perfil.

#### **>>>Configurando um ambiente virtual no VSCode<<<**

python -m venv env

ctrl+shift+p <br />
'select interpreter' - Python: Select Interpreter <br />
Selecione o python virtual que acabou de criar

# **>>>Criando um projeto django<<<**

Projeto django é um conjunto de arquivos que são
gerados automaticamente pelo django. Você pode
acicionar vários aplicativos ao projeto.

No terminal (env) digite:
django-admin startproject mysite . 
#Espaço e ponto significa a pasta atual.
Depois digite: python manage.py migrate

# **>>>Criando um usuário administrador<<<**

no terminal (env) digite:
python manage.py createsuperuser

# **>>>Criando um app vazio<<<**

No terminal (env) digite:
python manage.py startapp blog #blog é o nome
Em mysite.py/settings.py> installed_apps, adicione
'blog'.

# **>>>Arquitetura de um app web Django<<<**

-Os arquivos modelos definem a estrutura da tabela do banco de
dados.

-Os arquivos URLs cuidam do enraizamento da URL. 
Ou seja, procurará por um URl armazenado no banco de dados/slug.

-O arquivo view recebe uma solicitação da web e retorna uma resposta da web. 
Esta resposta pode ser o conteúdo HTML de uma página da Web.

-Interface admnistrativa pode ser usada para executar operações de criação, 
leitura, atualização e exclusão no modelo diretamente.

# **>>>Processos para criar um app<<<**

1- Criar HTML
2- Configurar URL
3- Criar views
4- Criar modelos
5- Conectar os processos

# **>>>Criando estrutura vazia do app<<<**

No terminal (env), digite:
python manage.py startapp nomedoseuapp

Em 'mysite/settings.py> INSTALLED_APPS', 
adicione 'translator'.

# **>>>Configurando URLs<<<**

Em 'mysite/urls.py' adicione:
path('seuapp/', include('seuapp.urls'))
