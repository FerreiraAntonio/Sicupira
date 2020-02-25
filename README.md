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

# Estrutura de dados do sistema Sicupira

![](https://www.lucidchart.com/publicSegments/view/486f446d-019e-48af-a495-183c24526d79/image.png)

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

# Equipe

| Papel           | Nome           | Avatar                                                                 | Participação | 
| --------------- | -------------- | ---------------------------------------------------------------------- | ------------ |
| Product Owner   | Ricardo Choren | ![](https://www.gravatar.com/avatar/00000000000000000000000000000000)  |              |
| Scrum Master    | Antonio Horta  | ![](https://www.gravatar.com/avatar/8e4c634fa51e80d59cad9fe9da5cbaf4)  | Planejamento, Prototipação, Modelagem, Documentação, Wiki, Apresentação |
| Modelagem       | Treice Moreira | ![](https://www.gravatar.com/avatar/b3d9451c693674676811851277c69b98)  | Modelagem |
| Modelagem       | Nicole Santos  | ![](https://www.gravatar.com/avatar/9e807b92146cb292cb311e5b449a8f64)  | Modelagem |
| Desenvolvimento | Gilvan Almeida | ![](https://www.gravatar.com/avatar/9d9a022baf8aaa57e60df7a6c076fcbe)  | Prototipação, Wiki |
| Desenvolvimento | Valdecir       | ![](https://www.gravatar.com/avatar/ee70d8d86a7bf46a23f88caf35e6ec14)  | Wiki |
| Desenvolvimento | Igor Maffei    | ![](https://www.gravatar.com/avatar/2952373d5701776691c1ac9e216ec3fb)  | Modelagem, Módulo Lattes, Wiki |
| Desenvolvimento |                |                                                                        | Sprint 1, Sprint 2  |
| Desenvolvimento |                |                                                                        | Sprint 3     |
| Desenvolvimento |                |                                                                        | Sprint 3     |
| Desenvolvimento |                |                                                                        | Sprint 2     |
| Testes          |                |                                                                        | Sprint 4     |
| Testes          |                |                                                                        | Sprint 4     |
| Testes          |                |                                                                        | Sprint 4     |
| Documentação    |                |                                                                        | Sprint 5     |
| Documentação    |                |                                                                        | Sprint 5     |
| Apresentação    |                |                                                                        | Apresentação |
| Apresentação    |                |                                                                        | Apresentação |


