from modelo.jogador import Jogador


class Jogada:

    def __init__(self, num_jogada: int, posicao_x: int, posicao_y: int, jogador: Jogador):
        self.__num_jogada = num_jogada
        self.__posicao = (posicao_x, posicao_y)
        self.__jogador = jogador

    def verifica_acerto(self):
        pass
