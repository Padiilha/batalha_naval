
from enum import Enum

class TipoNavio(Enum):
    SUBMARINO = 1
    FRAGATA = 2
    PORTA_AVIOES = 5


class Navio():
    def __init__(self, id, tipo: TipoNavio):
        self.id = id
        self.tipo = tipo

navio = Navio(10, TipoNavio.SUBMARINO)

navio.tipo.value
navio.tipo.name + ".jpg"

class Mapa:
    def __init__(self, tamanho_x, tamanho_y):
        self.__id = id
        self.__tamanho = tamanho_x * tamanho_y
        self.__quantidade_navios = 0
        self.__navios = []
        self.__area_navio = [[]]

    @property
    def id(self):
        return self.__id

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, x, y):
        self.__tamanho = x * y

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

