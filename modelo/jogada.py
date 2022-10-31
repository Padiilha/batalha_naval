from modelo.jogador import Jogador
from modelo.mapa import Mapa


class Jogada:

    def __init__(self,
                 num_jogada: int,
                 linha: int,
                 coluna: int,
                 jogador: Jogador,
                 mapa: Mapa):
        self.__num_jogada = num_jogada
        self.__posicao = (linha, coluna)
        self.__jogador = jogador
        self.__mapa = mapa

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
        if self.__mapa.tabuleiro[self.__posicao[0]][self.__posicao[1]] == '~':
            self.__mapa.tabuleiro[self.__posicao[0]][self.__posicao[1]] = '~'
            self.__mapa.tabuleiro_para_jogadores[self.__posicao[0]][self.__posicao[1]] = 'X'
            return False
        elif self.__mapa.tabuleiro[self.__posicao[0]][self.__posicao[1]] != '~' and self.__mapa.tabuleiro[self.__posicao[0]][self.__posicao[1]] != '*':
            self.__mapa.tabuleiro[self.__posicao[0]][self.__posicao[1]] = '*'
            self.__mapa.tabuleiro_para_jogadores[self.__posicao[0]][self.__posicao[1]] = '*'
            return True


#Acertar Lógica
    def fim_jogo(self) -> bool:
        linha = 0
        qtLinhas = len(self.__mapa.tabuleiro)
        while linha < qtLinhas:
            col = 0
            qtCol = len(self.__mapa.tabuleiro[linha])
            while col < qtCol:
                if self.__mapa.tabuleiro[linha][col] != '~' and self.__mapa.tabuleiro[linha][col] != '*':
                    return False
                col += 1
            linha += 1

        return True
