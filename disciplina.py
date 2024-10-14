from curso import Curso
import random

class Disciplina:
    """  Classe que representa o disciplina """

    def __init__(self
                 ,  curso_nome
                 ,  curso_codigo
                 ,  disciplina_codigo
                 ,  tipo
                 ,  carga_horaria_prevista
                 ,  disciplina_nome
                 ,  lista_atividades
    ) -> None:
        """ Construtor da classe disciplina """
        self.curso_nome                 = curso_nome
        self.curso_codigo               = curso_codigo
        self.disciplina_codigo          = disciplina_codigo
        self.tipo                       = tipo
        self.carga_horaria_prevista     = carga_horaria_prevista
        self.disciplina_nome            = disciplina_nome
        self.frequencia_minima          = 0.75 * carga_horaria_prevista
        self.nota_corte                 = 70
        self.lista_atividades           = lista_atividades

    @staticmethod
    def gerar_nota_disciplina():
        # Definir os intervalos
        numeros = list(range(101))
        
        # Atribuir pesos maiores para os números acima de 70
        pesos = [1 if i <= 70 else 5 for i in numeros]
        
        # Gerar um número com base nos pesos
        return random.choices(numeros, pesos, k=1)[0]

    @staticmethod
    def gerar_frequencia_disciplina():
        # Definir os intervalos
        numeros = list(range(101))
        
        # Atribuir pesos maiores para os números acima de 70
        pesos = [1 if i <= 70 else 5 for i in numeros]
        
        # Gerar um número com base nos pesos
        return random.choices(numeros, pesos, k=1)[0]

    @staticmethod
    def busca_lista_disciplinas_disponiveis():
        """ Retorna lista de disciplinas disponiveis """
        lista = []
        lista_cursos_disponiveis = Curso.busca_lista_cursos_disponiveis()
        id = Disciplina.gerador_id_disciplinas()

        for curso_disponivel in lista_cursos_disponiveis:

            curso_nome              = curso_disponivel.curso_nome
            curso_codigo            = curso_disponivel.curso_codigo
            carga_horaria_minima    = 16
            carga_horaria_maxima    = curso_disponivel.carga_horaria_por_disciplina_max

            if curso_nome == "Engenharia de Computação":
                lista_atividades = [
                    {'periodo': f'{random.choice(['01', '02'])}/{random.choice(['2024', '2023', '2022'])}', 'codigo_atividade': 1, 'nome_atividade': 'exercicio' },
                    {'periodo': f'{random.choice(['01', '02'])}/{random.choice(['2024', '2023', '2022'])}', 'codigo_atividade': 2, 'nome_atividade': 'trabalho01' },
                    {'periodo': f'{random.choice(['01', '02'])}/{random.choice(['2024', '2023', '2022'])}', 'codigo_atividade': 3, 'nome_atividade': 'trabalho02' },
                    {'periodo': f'{random.choice(['01', '02'])}/{random.choice(['2024', '2023', '2022'])}', 'codigo_atividade': 4, 'nome_atividade': 'avaliacao' },
                ]
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                                random.randint(carga_horaria_minima, carga_horaria_maxima), 'Cálculo Diferencial e Integral', lista_atividades))
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                                random.randint(carga_horaria_minima, carga_horaria_maxima), 'Álgebra Linear', lista_atividades))
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                                random.randint(carga_horaria_minima, carga_horaria_maxima), 'Eletrônica Digital', lista_atividades))
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                                random.randint(carga_horaria_minima, carga_horaria_maxima), 'Sistemas Operacionais', lista_atividades))
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                                random.randint(carga_horaria_minima, carga_horaria_maxima), 'Programação de Computadores', lista_atividades))

            if curso_nome == "Ciencia da Computação":
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                                random.randint(carga_horaria_minima, carga_horaria_maxima), 'Teoria da Computação', lista_atividades))
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                                random.randint(carga_horaria_minima, carga_horaria_maxima), 'Cálculo Diferencial e Integral', lista_atividades))
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                                random.randint(carga_horaria_minima, carga_horaria_maxima), 'Compiladores', lista_atividades))
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                                random.randint(carga_horaria_minima, carga_horaria_maxima), 'Matemática Discreta', lista_atividades))
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                                random.randint(carga_horaria_minima, carga_horaria_maxima), 'Análise de Algoritmos', lista_atividades))

            if curso_nome == "Sistemas de Informação":
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                                random.randint(carga_horaria_minima, carga_horaria_maxima), 'Algoritmos e Estruturas de Dados', lista_atividades))
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                                random.randint(carga_horaria_minima, carga_horaria_maxima), 'Fundamentos de Programação', lista_atividades))
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                                random.randint(carga_horaria_minima, carga_horaria_maxima), 'Banco de Dados', lista_atividades))
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                                random.randint(carga_horaria_minima, carga_horaria_maxima), 'Engenharia de Software', lista_atividades))
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                                random.randint(carga_horaria_minima, carga_horaria_maxima), 'Sistemas Operacionais', lista_atividades))

            if curso_nome == "Jogos Digitais":
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                                random.randint(carga_horaria_minima, carga_horaria_maxima), 'Modelagem 3D', lista_atividades))
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                                random.randint(carga_horaria_minima, carga_horaria_maxima), 'Inteligência Artificial para Jogos', lista_atividades))
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                                random.randint(carga_horaria_minima, carga_horaria_maxima), 'Efeitos Visuais', lista_atividades))
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                                random.randint(carga_horaria_minima, carga_horaria_maxima), 'Jogos em Realidade Aumentada (AR) e Virtual (VR)', lista_atividades))
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                                random.randint(carga_horaria_minima, carga_horaria_maxima), 'Psicologia Cognitiva Aplicada a Jogos', lista_atividades))

            if curso_nome == "Tecnologo Rede Digitais":
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                            random.randint(carga_horaria_minima, carga_horaria_maxima), 'Administração de Servidores', lista_atividades))
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                            random.randint(carga_horaria_minima, carga_horaria_maxima), 'Protocolos de Redes', lista_atividades))
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                            random.randint(carga_horaria_minima, carga_horaria_maxima), 'Gerência de Projetos de TI', lista_atividades))
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                            random.randint(carga_horaria_minima, carga_horaria_maxima), 'Redes Definidas por Software (SDN)', lista_atividades))
                lista.append(Disciplina(curso_nome, curso_codigo, next(id), random.choices(['teorico', 'pratico'], weights=[85,15], k=1)[0], 
                            random.randint(carga_horaria_minima, carga_horaria_maxima), 'Cloud Computing (Computação em Nuvem)', lista_atividades))

        return lista
    
    @classmethod
    def gerador_id_disciplinas(cls):
        """ Gerar IDs para as disciplinas """
        numero = 1
        while True:
            yield numero
            numero += 1
