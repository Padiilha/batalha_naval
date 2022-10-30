from modelo.jogada import Jogada
from modelo.jogador import Jogador
from modelo.mapa import Mapa
from modelo.partida import Partida
from visualizacao.tela_partida import TelaPartida


class ControladorPartida:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__partidas = list()
        self.__tela_partida = TelaPartida()
        self.__id = 1

    def inicia_partida(self):
        dados_partida = self.__tela_partida.inicia_partida()
        # pegar Jogador com ID == dados_partida[0]
        # pegar Jogador com ID == dados_partida[1]
        # pegar Mapa com ID == dados_partida[2]
        partida = Partida(self.__id,
                          jogador1,
                          jogador2,
                          mapa)
        self.__id += 1
        self.__partidas.append(partida)
        num_jogada = 1
        while True:
            if num_jogada % 2 == 1:
                jogador_vez = jogador1
            else:
                jogador_vez = jogador2
            posicao = self.__tela_partida.faz_jogada(num_jogada)
            jogada = Jogada(num_jogada,
                            posicao[0],
                            posicao[1],
                            jogador_vez)
            num_jogada += 1
            partida.conta_jogada()
            partida.adiciona_jogada(jogada)
            if jogada.verifica_acerto():
                partida.adiciona_acerto(jogada)
            if jogada.fim_jogo():
                partida.vencedor = jogador_vez
                break

    def lista_partida(self):
        for partida in self.__partidas:
            dados_partida = [partida.id,
                             partida.jogadores,
                             partida.mapa,
                             partida.jogadas,
                             partida.acertos,
                             partida.total_jogadas,
                             partida.vencedor]
            self.__tela_partida.lista_partida(dados_partida)

    def mostra_tela_opcoes(self):
        opcoes = {1: self.inicia_partida,
                  2: self.lista_partida}
        while True:
            opcao = self.__tela_partida.mostra_opcoes()
            if opcao == 0:
                break
            opcoes[opcao]()
