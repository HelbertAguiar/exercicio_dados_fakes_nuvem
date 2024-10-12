from aluno import Aluno
from curso import Curso
from disciplina import Disciplina
from pprint import pprint
import random
import pandas as pd
import csv

def gerar_csv_com_pandas(nome_arquivo, dados, colunas):
    """Função para gerar arquivos CSV usando pandas."""
    df = pd.DataFrame(dados, columns=colunas)
    df.to_csv(nome_arquivo, index=False, encoding='utf-8')

lista_cursos_disponiveis = Curso.busca_lista_cursos_disponiveis()
lista_disciplinas_disponiveis = Disciplina.busca_lista_disciplinas_disponiveis()
lista_aluno = Aluno.gera_aluno_aleatorio(quantidade = 2)
lista_relacionamento_cursos_disciplinas_alunos = []
tipos_atividades = ['exercicio', 'trabalho', 'avaliacao']
lista_atividades_alunos = []

# Gerar relações entre alunos, cursos e disciplinas
for aluno in lista_aluno:

    curso = random.choice(lista_cursos_disponiveis)
    disciplina = random.choice([disciplina for disciplina in lista_disciplinas_disponiveis 
                                if disciplina.curso_codigo == curso.curso_codigo])
    
    # Adiciona o relacionamento na lista
    nota_aluno = Disciplina.gerar_nota_disciplina()
    frequencia = Disciplina.gerar_frequencia_disciplina()
    periodo = f'{random.choice(['01', '02'])}/{random.choice(['2024', '2023', '2022'])}'
    if nota_aluno >= 70 and frequencia >= 75: 
        situacao = 'aprovado'
    elif nota_aluno < 70 and nota_aluno >= 60 and frequencia >= 75: 
        situacao = 'exame_especial'
    else: 
        situacao = 'reprovado'
    
    lista_relacionamento_cursos_disciplinas_alunos.append({
        'curso_nome'            : curso.curso_nome,
        'curso_codigo'          : curso.curso_codigo,
        'disciplina_codigo'     : disciplina.disciplina_codigo,
        'periodo'               : periodo,
        'aluno_matricula'       : aluno.curso_matricula_aluno,
        'aluno_nome_completo'   : aluno.nome_completo,
        'nota_aluno'            : nota_aluno,
        'status'                : situacao,
        'frequencia_aluno'      : frequencia
    })

    # Gerar atividades para o aluno
    for codigo_atividade in range(1, random.randint(2, 6)):  # Cada aluno tem de 2 a 5 atividades
        tipo_atividade = random.choice(tipos_atividades)
        valor_atividade = random.randint(5, 20)  # Valor entre 5 e 20 pontos
        nota_obtida = random.randint(0, valor_atividade)  # Nota aleatória até o valor máximo da atividade
        
        # Adiciona atividade à lista de atividades
        lista_atividades_alunos.append({
            'aluno_matricula': aluno.curso_matricula_aluno,
            'curso_codigo': curso.curso_codigo,
            'disciplina_codigo': disciplina.disciplina_codigo,
            'periodo': periodo,
            'codigo_atividade': codigo_atividade,
            'nome_atividade': tipo_atividade,
            'valor_atividade': valor_atividade,
            'nota_obtida': nota_obtida
        })


pprint(lista_cursos_disponiveis)
pprint(lista_disciplinas_disponiveis)
pprint(lista_aluno)
pprint(lista_relacionamento_cursos_disciplinas_alunos)
pprint(lista_atividades_alunos)