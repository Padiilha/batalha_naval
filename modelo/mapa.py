
class Mapa:
    def __init__(self, id, tabuleiro, tabuleiro_para_jogadores, linhas: int, colunas: int, quantidade_navios):
        self.__id = id
        self.__tabuleiro = tabuleiro
        self.__tabuleiro_para_jogadores = tabuleiro_para_jogadores
        self.__linhas = linhas
        self.__colunas = colunas
        self.__quantidade_navios = quantidade_navios
        self.__navios = []

    @property
    def id(self):
        return self.__id

    @property
    def linhas(self):
        return self.__linhas

    @linhas.setter
    def linhas(self, linhas):
        self.__linhas = linhas

    @property
    def colunas(self):
        return self.__colunas

    @colunas.setter
    def colunas(self, colunas):
        self.__colunas = colunas

    @property
    def tabuleiro(self):
        return self.__tabuleiro

    @tabuleiro.setter
    def tabuleiro(self, tabuleiro):
        self.__tabuleiro = tabuleiro

    @property
    def tabuleiro_para_jogadores(self):
        return self.__tabuleiro_para_jogadores

    @tabuleiro_para_jogadores.setter
    def tabuleiro_para_jogadores(self, tabuleiro_para_jogadores):
        self.__tabuleiro_para_jogadores = tabuleiro_para_jogadores

    @property
    def navios(self):
        return self.__navios

    @navios.setter
    def navios(self, navios):
        self.__navios = navios

    @property
    def area_navio(self):
        return self.__area_navio

    @area_navio.setter
    def area_navio(self, area_navio):
        self.__area_navio = area_navio




