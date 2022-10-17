

class Jogador:

    def __init__(self, nome: str):
        self.__nome = nome
        self.__total_pontos = 0
        self.__posicao_ranking = 0
        self.__qtd_jogos = 0
        self.__qtd_vitorias = 0

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def total_pontos(self) -> int:
        return self.__total_pontos

    @total_pontos.setter
    def total_pontos(self, pontos: int):
        self.__total_pontos += pontos

    @property
    def posicao_ranking(self) -> int:
        return self.__posicao_ranking

    @posicao_ranking.setter
    def posicao_ranking(self, posicao_ranking: int):
        self.__posicao_ranking = posicao_ranking

    @property
    def qtd_jogos(self) -> int:
        return self.__qtd_jogos

    @qtd_jogos.setter
    def qtd_jogos(self):
        self.__qtd_jogos += 1

    @property
    def qtd_vitorias(self) -> int:
        return self.__qtd_vitorias

    @qtd_vitorias.setter
    def qtd_vitorias(self):
        self.__qtd_vitorias += 1
