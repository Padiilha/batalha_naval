from modelo.jogador import Jogador
from modelo.mapa import Mapa
from modelo.jogada import Jogada


class Partida:

    def __init__(self, id):
        self.__id = id
        self.__jogadores = list()
        self.__mapa = Mapa()
        self.__jogadas = list()
        self.__acertos = list()
        self.__total_jogadas = 0
        self.__vencedor = Jogador()

    def id(self) -> int:
        return self.__id

    def jogadores(self) -> list:
        return self.__jogadores

    def adiciona_jogadores(self, jogador1: Jogador, jogador2: Jogador):
        self.__jogadores.append(jogador1)
        self.__jogadores.append(jogador2)

    @property
    def mapa(self) -> Mapa:
        return self.__mapa

    @mapa.setter
    def mapa(self, mapa: Mapa):
        self.__mapa = mapa

    def jogadas(self) -> list:
        return self.__jogadas

    def adiciona_jogada(self, jogada: Jogada):
        self.__jogadas.append(jogada)

    def acertos(self) -> list:
        return self.__acertos

    def adiciona_acerto(self, acerto: Jogada):
        self.__acertos.append(acerto)

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
