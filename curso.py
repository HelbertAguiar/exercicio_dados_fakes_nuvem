class Curso:
    """  Classe que representa o curso """

    def __init__(self
                 ,  curso_nome
                 ,  curso_codigo
                 ,  quantidade_periodos
                 ,  carga_horaria_por_disciplina_max
                 ,  disciplinas_por_periodo
                 ,  media_alunos_turma
    ) -> None:
        """ Construtor da classe curso """
        self.nome_instituicao               = "Faculdade Prodata"
        self.curso_nome                     = curso_nome
        self.curso_codigo                   = curso_codigo
        self.quantidade_periodos            = quantidade_periodos
        self.carga_horaria_por_disciplina_max   = carga_horaria_por_disciplina_max
        self.disciplinas_por_periodo        = disciplinas_por_periodo
        self.media_alunos_turma             = media_alunos_turma

    @staticmethod
    def busca_lista_cursos_disponiveis():
        """ Retorna lista de cursos disponiveis """
        lista = []
        lista.append(Curso("Engenharia de Computação", 1, 10, 92, 8, 50))
        lista.append(Curso("Ciencia da Computação", 2, 8, 64, 8, 62))
        lista.append(Curso("Sistemas de Informações", 3, 8, 64, 7, 48))
        lista.append(Curso("Jogos Digitais", 4, 6, 48, 6, 32))
        lista.append(Curso("Tecnologo Rede Digitais", 5, 4, 48, 6, 28))
        return lista

