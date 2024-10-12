from faker import Faker
from datetime import datetime
from curso import Curso
import random

class Aluno:
    """ Classe que representa o aluno """
    
    def __init__(self
                 ,  nome_completo
                 ,  sexo
                 ,  cpf
                 ,  data_nascimento
                 ,  email
                 ,  endereco_cidade
                 ,  endereco_estado
                 ,  curso_matricula_aluno
                 ,  curso_codigo
                 ,  curso_data_ingresso
                 ,  curso_data_prevista_conclusao
                 ,  curso_data_conclusao
                 ,  curso_situacao_matricula

    ) -> None:
        """ Construtor da classe aluno """
        
        self.nome_completo                      = nome_completo
        self.sexo                               = sexo
        self.cpf                                = cpf
        self.data_nascimento                    = data_nascimento
        self.email                              = email
        self.endereco_cidade                    = endereco_cidade
        self.endereco_estado                    = endereco_estado
        self.curso_matricula_aluno              = curso_matricula_aluno
        self.curso_codigo                       = curso_codigo
        self.curso_data_ingresso                = curso_data_ingresso
        self.curso_data_prevista_conclusao      = curso_data_prevista_conclusao
        self.curso_data_conclusao               = curso_data_conclusao
        self.curso_situacao_matricula           = curso_situacao_matricula

    @staticmethod
    def gera_aluno_aleatorio(quantidade = 1):

        localizacao = 'pt-BR'
        fake = Faker(locale=localizacao)
        sexo = random.choice(['m', 'f'])
        lista = []

        for _ in range(quantidade):

            lista.append(
                Aluno(
                        nome_completo=fake.name_male() if sexo == 'm' else fake.name_female()
                    ,   sexo=sexo
                    ,   cpf=fake.cpf()
                    ,   data_nascimento=fake.date_between(
                            start_date=datetime(1980, 1, 1), end_date=datetime(2006, 1, 1)
                        )
                    ,   email=fake.email()
                    ,   endereco_cidade=fake.city()
                    ,   endereco_estado=fake.state()
                    ,   curso_matricula_aluno=fake.random_number(digits=6, fix_len=True)
                    ,   curso_codigo=random.choice(Curso.busca_lista_cursos_disponiveis()).curso_codigo
                    ,   curso_data_ingresso=fake.date_between(
                            start_date=datetime(2023, 1, 1), end_date='today'
                        )
                    ,   curso_data_prevista_conclusao=fake.date_between(
                            start_date=datetime(2024, 12, 1), end_date=datetime(2026, 12, 31)
                        )
                    ,   curso_data_conclusao=None
                    ,   curso_situacao_matricula=random.choices(
                                ['ativo', 'trancado', 'cancelado']
                            ,   weights=[85,10,5]
                            ,   k=1
                        )[0]
            )) 

        return lista
        