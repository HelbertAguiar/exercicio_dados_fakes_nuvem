from aluno import Aluno
from curso import Curso
from disciplina import Disciplina
import random
import pandas as pd
import os

def salva_lista_para_csv(lista, nome_arquivo):
    # Verifica se a lista está vazia
    if not lista:
        print("A lista está vazia, nada para salvar.")
        return
    
    # Verifica se o primeiro item da lista é um dicionário
    if isinstance(lista[0], dict):
        # Cria um DataFrame diretamente da lista de dicionários
        df = pd.DataFrame(lista)
    else:
        # Extrai as propriedades dinamicamente do primeiro objeto
        propriedades = vars(lista[0]).keys()
        
        # Cria uma lista de dicionários com as propriedades de cada objeto
        dados = [{prop: getattr(obj, prop) for prop in propriedades} for obj in lista]
        
        # Cria o DataFrame a partir dessa lista de dicionários
        df = pd.DataFrame(dados)

    # Define o caminho da pasta "arquivos"
    caminho_pasta = os.path.join(os.getcwd(), "arquivos")
    
    # Verifica se a pasta "arquivos" existe, caso contrário, cria a pasta
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)
    
    # Define o caminho completo do arquivo CSV
    caminho_arquivo = os.path.join(caminho_pasta, f"{nome_arquivo}")
    
    # Salva o DataFrame em um arquivo CSV com BOM para evitar problemas de encoding no Excel
    df.to_csv(caminho_arquivo, index=False, encoding='utf-8-sig')
    
    print(f"DataFrame salvo com sucesso em: {caminho_arquivo}")

lista_cursos_disponiveis = Curso.busca_lista_cursos_disponiveis()
lista_disciplinas_disponiveis = Disciplina.busca_lista_disciplinas_disponiveis()
lista_aluno = Aluno.gera_aluno_aleatorio(quantidade = 500)
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
    motivo_reprovacao = 'n/a'
    if nota_aluno >= 70 and frequencia >= 75: 
        situacao = 'aprovado'
    elif nota_aluno < 70 and nota_aluno >= 60 and frequencia >= 75: 
        situacao = 'exame_especial'
    else: 
        situacao = 'reprovado'
        if frequencia < 75: 
            motivo_reprovacao = 'frequencia'
        else:
            motivo_reprovacao = 'nota'
    
    lista_relacionamento_cursos_disciplinas_alunos.append({
        'curso_nome'            : curso.curso_nome,
        'curso_codigo'          : curso.curso_codigo,
        'disciplina_codigo'     : disciplina.disciplina_codigo,
        'periodo'               : periodo,
        'aluno_matricula'       : aluno.curso_matricula_aluno,
        'aluno_nome_completo'   : aluno.nome_completo,
        'nota_aluno'            : nota_aluno,
        'status'                : situacao,
        'frequencia_aluno'      : frequencia,
        'motivo_reprovacao'     : motivo_reprovacao
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

# Criando o DataFrame dinamicamente
salva_lista_para_csv(lista_cursos_disponiveis, 'cursos.csv')
salva_lista_para_csv(lista_disciplinas_disponiveis, 'disciplinas.csv')
salva_lista_para_csv(lista_aluno, 'alunos.csv')
salva_lista_para_csv(lista_relacionamento_cursos_disciplinas_alunos, 'relacionamento_alunos_cursos_disciplinas.csv')
salva_lista_para_csv(lista_atividades_alunos, 'atividades_alunos.csv')

