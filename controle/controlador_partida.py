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
        jogador1 = self.__controlador_principal.pega_jogador_por_id(dados_partida[0])
        jogador2 = self.__controlador_principal.pega_jogador_por_id(dados_partida[1])
        mapa = self.__controlador_principal.pega_mapa_por_tamanho(dados_partida[2])
        partida = Partida(self.__id,
                          jogador1,
                          jogador2,
                          mapa)
        self.__id += 1
        self.__partidas.append(partida)
        jogador1.adiciona_jogo()
        jogador2.adiciona_jogo()
        num_jogada = 1
        while True:
            if num_jogada % 2 == 1:
                jogador_vez = jogador1
            else:
                jogador_vez = jogador2
            self.__controlador_principal.mostra_mapa(partida.mapa.tabuleiro_para_jogadores)
            posicao = self.__tela_partida.faz_jogada(num_jogada)
            jogada = Jogada(num_jogada,
                            posicao[0],
                            posicao[1],
                            jogador_vez,
                            partida.mapa)

            num_jogada += 1
            partida.conta_jogada()
            partida.adiciona_jogada(jogada)
            if jogada.verifica_acerto():
                partida.adiciona_acerto(jogada)
                jogador_vez.adiciona_ponto()
            if jogada.fim_jogo():
                partida.vencedor = jogador_vez
                jogador_vez.adiciona_vitoria()
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
