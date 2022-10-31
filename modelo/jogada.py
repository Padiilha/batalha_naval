from modelo.jogador import Jogador


class Jogada:

    def __init__(self,
                 num_jogada: int,
                 linha: int,
                 coluna: int,
                 jogador: Jogador):
        self.__num_jogada = num_jogada
        self.__posicao = (linha, coluna)
        self.__jogador = jogador

    @property
    def num_jogada(self) -> int:
        return self.__num_jogada

    @property
    def posicao(self) -> tuple:
        return self.__posicao

    @property
    def jogador(self) -> Jogador:
        return self.__jogador

    def verifica_acerto(self) -> bool:
        # verifica se self.__posicao no Mapa é 0 ou 1
        # se 1, muda pra 0 e retorna True
        pass

    def fim_jogo(self) -> bool:
        # percorre o Mapa, se ocorrer 1 = False
        pass
