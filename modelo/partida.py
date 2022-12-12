from modelo.jogador import Jogador
from modelo.mapa import Mapa
from modelo.jogada import Jogada


class Partida:

    def __init__(self,
                 id: int,
                 jogador1: Jogador,
                 jogador2: Jogador,
                 mapa: Mapa):
        self.__id = id
        self.__jogadores = [jogador1, jogador2]
        self.__mapa = mapa
        self.__jogadas = list()
        self.__acertos = list()
        self.__total_jogadas = 0
        self.__vencedor = Jogador

    @property
    def id(self) -> int:
        return self.__id

    @property
    def jogadores(self) -> list:
        return self.__jogadores

    @property
    def mapa(self) -> Mapa:
        return self.__mapa

    @property
    def jogadas(self) -> list:
        return self.__jogadas

    def adiciona_jogada(self, jogada: Jogada):
        self.__jogadas.append(jogada)

    @property
    def acertos(self) -> list:
        return self.__acertos

    def adiciona_acerto(self, acerto: Jogada):
        self.__acertos.append(acerto)

    @property
    def total_jogadas(self) -> int:
        return self.__total_jogadas

    def conta_jogada(self):
        self.__total_jogadas += 1

    @property
    def vencedor(self) -> Jogador:
        return self.__vencedor

    @vencedor.setter
    def vencedor(self, vencedor: Jogador):
        self.__vencedor = vencedor
