from modelo.jogador import Jogador
from modelo.mapa import Mapa
from modelo.jogada import Jogada


class Partida:
    def __init__(self):
        self.__id = id
        self.__jogadores = list()
        self.__mapa = Mapa()
        self.__jogadas = list()
        self.__acertos = list()
        self.__total_jogadas = 0
        self.__vencedor = Jogador()

    def jogadores(self) -> list:
        return self.__jogadores

    def jogadores(self, jogador: Jogador):
        self.__jogadores.append(jogador)

    @property
    def mapa(self) -> Mapa:
        return self.__mapa

    @mapa.setter
    def mapa(self, mapa: Mapa):
        self.__mapa = mapa

    def jogadas(self) -> list:
        return self.__jogadas

    def jogadas(self, jogada: Jogada):
        self.__jogadas.append(jogada)

    def acertos(self) -> list:
        return self.__acertos

    def acertos(self, acerto: Acerto):
        self.__acertos.append(acerto)

    def total_jogadas(self) -> int:
        return self.__total_jogadas

    def total_jogadas(self):
        self.__total_jogadas += 1

    @property
    def vencedor(self) -> Jogador:
        return self.__vencedor

    @vencedor.setter
    def vencedor(self, vencedor: Jogador):
        self.__vencedor = vencedor

    def inicia_partida(self):
        pass
