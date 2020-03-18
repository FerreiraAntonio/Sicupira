#from lxml import objectify
#import untangle
import xmltodict
from django.db.models import Q
from pessoa.models import Pessoa
from pessoa.models import Abreviatura
from sicupira.models import Pais
from datetime import date
from django.db import DatabaseError, transaction

class LattesService:
    @staticmethod
    def importXML(xml):
        obj = xmltodict.parse(xml, process_namespaces=True)

        #pessoa = Pessoa.objects.create(nome=obj['CURRICULO-VITAE']['DADOS-GERAIS']['@NOME-COMPLETO'])
        pessoa = Pessoa()
        try:
            with transaction.atomic():
                pessoa.nome = obj['CURRICULO-VITAE']['DADOS-GERAIS']['@NOME-COMPLETO']
                pessoa.sexo = 'M'
                pessoa.data_nascimento = date(1977,3,3)
                pessoa.numero_documento = '07758079741'
                pessoa.email = 'igormaffei@gmail.com'

                # Tratamento de país
                paises = Pais.objects.filter(Q(nome_pais=obj['CURRICULO-VITAE']['DADOS-GERAIS']['@PAIS-DE-NACIONALIDADE']))
                if paises.exists():
                    print(paises[0])
                    pessoa.nacionalidade = paises[0]

                pessoa.save()
                # tratamento de abreviação
                abrevs = obj['CURRICULO-VITAE']['DADOS-GERAIS']['@NOME-EM-CITACOES-BIBLIOGRAFICAS']
                if abrevs:
                    first = True
                    items = abrevs.split(';')
                    print(items)
                    for item in items:
                        Abreviatura.objects.create(pessoa=pessoa,
                                                   desc_abreviatura=item,
                                                   flg_principal= first if 1 else 0)

            return pessoa
        except:
            return None

    @staticmethod
    def save(obj):
        pass