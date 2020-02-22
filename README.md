# Projeto Sicupira

Projeto desenvolvido como forma de avaliação da disciplina de DSC do IME 2020. O objetivo é desenvolver um sistema inspirado no Sucupira da CAPES com os módulos de Dados Cadastrais do Programa, Linhas de pesquisa, Turmas, Docentes e Discentes.

# Escopo do programa

Dentro de https://sucupira.capes.gov.br/sucupira/
Opção Coleta Capes

Dados cadastrais
Linha de pesquisa
Disciplinas
Turmas
Docentes*
Discentes*
*Com preenchimento automático pela integração da plataforma lattes


# Executando o sistema

Tenha certeza que o python está instalado no sistema


Faça download do repositório

```

git clone https://gitlab.com/ime-dsc-2020/sicupira.git
cd sucupira
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt

```

Crie o banco de dados

```

./manage.py makemigrations
./manage.py migrate

```

Crie um superusuario

```

./manage.py createsuperuser

```

Execute o servidor

```

./manage.py runserver

```

chame no browser http://127.0.0.01:8000

Efetue o login com as credenciais criadas

# Admin

O Admin pode ser acessado para gerenciar usuários e tabelas através da url:

http://127.0.0.01:8000/admin

