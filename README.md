# Projeto Sicupira

Projeto desenvolvido como forma de avaliação da disciplina de DSC do IME 2020. O objetivo é desenvolver um sistema inspirado no Sucupira da CAPES com os módulos de Dados Cadastrais do Programa, Linhas de pesquisa, Turmas, Docentes e Discentes.

# Escopo do programa

Dentro de https://sucupira.capes.gov.br/sucupira/

## Opção Coleta Capes

* Dados cadastrais
* Linha de pesquisa
* Disciplinas
* Turmas
* Docentes*
* Discentes*

*Com preenchimento automático pela integração da plataforma lattes

# Demo

O DEMO do projeto está disponível em [https://ajhorta.pythonanywhere.com](https://ajhorta.pythonanywhere.com)

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

rm -Rf db.sqlite3
rm -Rf ./pessoa/migrations/*
rm -Rf ./sicupira/migrations/*

./manage.py makemigrations sicupira
./manage.py makemigrations pessoa
./manage.py migrate

```

Crie um superusuario

```

./manage.py createsuperuser

```

Caso de a carga inicial no banco de dados com as tabelas auxiliares


```

./manage.py loaddata ./fixtures/db.json 

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

# Equipe

| Papel           | Nome           | Avatar                                                                 | Participação | 
| --------------- | -------------- | ---------------------------------------------------------------------- | ------------ |
| Product Owner   | Ricardo Choren | ![](https://www.gravatar.com/avatar/00000000000000000000000000000000)  |              |
| PM/Scrum Master | Antonio Horta  | ![](https://www.gravatar.com/avatar/8e4c634fa51e80d59cad9fe9da5cbaf4)  | Planejamento, Prototipação, Modelagem, Documentação, Wiki, Apresentação |
| Modelagem       | Treice Moreira | ![](https://www.gravatar.com/avatar/b3d9451c693674676811851277c69b98)  | Modelagem |
| Modelagem       | Nicole Santos  | ![](https://www.gravatar.com/avatar/9e807b92146cb292cb311e5b449a8f64)  | Modelagem, Documentação |
| Modelagem   | Ricardo Lopes  | ![](https://www.gravatar.com/avatar/00000000000000000000000000000000)  | Modelagem, MER |
| Modelagem   | Ricardo Villafan | ![](https://www.gravatar.com/avatar/00000000000000000000000000000000)  | Modelagem, MER |
| Desenvolvimento | Gilvan Almeida | ![](https://www.gravatar.com/avatar/9d9a022baf8aaa57e60df7a6c076fcbe)  | Prototipação, Wiki |
| Desenvolvimento | Valdecir       | ![](https://www.gravatar.com/avatar/ee70d8d86a7bf46a23f88caf35e6ec14)  | Wiki, Desenvolvimeto |
| Desenvolvimento | Igor Maffei    | ![](https://www.gravatar.com/avatar/2952373d5701776691c1ac9e216ec3fb)  | Modelagem, Módulo Lattes, Wiki |
| Desenvolvimento | Guilherme Bernieri  | ![](https://www.gravatar.com/avatar/dba1855aee0c6b1debf88d02bf2f3ada)  | Linha de Pesquisa, Wiki  |
| Desenvolvimento | Rafael Macedo  | ![](https://www.gravatar.com/avatar/00000000000000000000000000000000)  | Turma, Wiki, Testes  |
| Desenvolvimento |                |                                                                        | Sprint 3     |
| Desenvolvimento | Antonio Ferreira |![](https://www.gravatar.com/avatar/00000000000000000000000000000000) | Sprint 2     |
| Testes          | Wagner Sodré   |                                                                        | Testes, Sprint 3 |
| Testes          | Mário Azevedo  | ![](https://www.gravatar.com/avatar/00000000000000000000000000000000) | Testes, Bugfix |
| Documentação    | Michelle Mesquita | ![](https://www.gravatar.com/avatar/00000000000000000000000000000000) | Documentação |
| Documentação    | Alessandro Rebello | ![](https://www.gravatar.com/avatar/00000000000000000000000000000000) | Documentação |
| Documentação    | Matheus Mattos | ![](https://www.gravatar.com/avatar/00000000000000000000000000000000) | Sprint 5     |
| Documentação    | Pedro Bernabé  | ![](https://www.gravatar.com/avatar/00000000000000000000000000000000) | Sprint 5     |
| Documentação    |     Diego      | ![](https://www.gravatar.com/avatar/00000000000000000000000000000000) | Sprint 5     |
| Apresentação    |                |                                                                        | Apresentação |
| Apresentação    |                |                                                                        | Apresentação |


