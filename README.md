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

# Template HTML (Layout do programa)

Acesse com o browser a estrutura do site em 

```
sicupira/sicupira/layout_html/index.html
´´´

# Executando o sistema
```
source myvenv/bin/activate
python manage.py nserver
´´´
chame no browser http://127.0.0.01:8000