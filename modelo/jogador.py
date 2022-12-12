

class Jogador:

    def __init__(self, id: int, nome: str):
        self.__id = id
        self.__nome = nome
        self.__total_pontos = 0
        self.__posicao_ranking = 0
        self.__qtd_jogos = 0
        self.__qtd_vitorias = 0

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def total_pontos(self) -> int:
        return self.__total_pontos

    def adiciona_ponto(self):
        self.__total_pontos += 1

    @property
    def posicao_ranking(self) -> int:
        return self.__posicao_ranking

    @posicao_ranking.setter
    def posicao_ranking(self, posicao_ranking: int):
        self.__posicao_ranking = posicao_ranking

    @property
    def qtd_jogos(self) -> int:
        return self.__qtd_jogos

    def adiciona_jogo(self):
        self.__qtd_jogos += 1

    @property
    def qtd_vitorias(self) -> int:
        return self.__qtd_vitorias

    def adiciona_vitoria(self):
        self.__qtd_vitorias += 1
