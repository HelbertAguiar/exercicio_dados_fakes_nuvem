-- FATO_HIST_ATIVIDADE
SELECT 
    aa.disciplina_codigo AS COD_DISCIPLINA,
    aa.codigo_atividade AS COD_ATIVIDADE,
    aa.curso_codigo AS COD_CURSO,
    aa.aluno_matricula AS MATRICULA_ALUNO,
    aa.periodo AS PERIODO,
    aa.valor_atividade AS VALOR_ATIVIDADE,
    aa.nota_obtida AS NOTA_OBTIDA,
    rd.frequencia_aluno AS FREQUENCIA_ALUNO,
    rd.status AS STATUS,
    rd.motivo_reprovacao AS MOTIVO_REPROVACAO
FROM "atividades_alunos"."datalake-1518501".raw."atividades_alunos" AS aa
INNER JOIN "relacionamento_alunos_cursos_disciplinas"."datalake-1518501".raw."relacionamento_alunos_cursos_disciplinas" AS rd 
ON aa.aluno_matricula = rd.aluno_matricula
AND aa.curso_codigo = rd.curso_codigo
AND aa.disciplina_codigo = rd.disciplina_codigo


--DIM_CURSO
SELECT 
    curso_codigo AS COD_CURSO,
    curso_nome AS NOME_CURSO,
    quantidade_periodos AS QUANTIDADE_PERIODO,
    carga_horaria_por_disciplina_max AS CARGA_HORARIA_PREVISTA,
    disciplinas_por_periodo as QTD_DISCIPLINA_PERIODO,
    media_alunos_turma AS MEDIA_ALUNO_TURMA,
    nome_instituicao AS NOME_INSTITUICAO
FROM cursos."datalake-1518501".raw.cursos

--DIM_ATIVIDADE
SELECT distinct
    codigo_atividade AS COD_ATIVIDADE,
    nome_atividade AS NOME_ATIVIDADE
FROM "atividades_alunos"."datalake-1518501".raw."atividades_alunos"

--DIM_DISCIPLINA
SELECT
    disciplina_codigo AS COD_DISCIPLINA,
    disciplina_nome AS NOME_DISCIPLINA,
    tipo AS TIPO,
    nota_corte AS NOTA_CORTE,
    carga_horaria_prevista AS CARGA_HORARIA_PREVISTA,
    frequencia_minima AS FREQUENCIA_MINIMA
FROM "disciplinas"."datalake-1518501".raw."disciplinas"

--DIM_ALUNO
SELECT 
    curso_matricula_aluno AS MATRICULA_ALUNO,
    cpf AS DOCUMENTO,
    nome_completo AS NOME_ALUNO,
    sexo AS SEXO,
    data_nascimento AS DATA_NASCIMENTO,
    email AS EMAIL,
    endereco_cidade AS CIDADE_ALUNO,
    endereco_estado AS ESTADO_ALUNO,
    telefone AS TELEFONE,
    curso_data_ingresso AS DATA_INGRESSO,
    curso_data_prevista_conclusao AS DATA_PREVISTA_CONCLUSAO,
    curso_data_conclusao AS DATA_CONCLUSAO,
    curso_situacao_matricula AS SITUACAO_ALUNO
FROM "alunos"."datalake-1518501".raw."alunos"