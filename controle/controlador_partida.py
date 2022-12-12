from modelo.jogada import Jogada
from modelo.partida import Partida
from visualizacao.tela_partida import TelaPartida


class ControladorPartida:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__partidas = []
        self.__tela_partida = TelaPartida()
        self.__id = 1

    def inicia_partida(self):
        dados_partida = self.__tela_partida.inicia_partida()
        jogador1 = self.__controlador_principal.pega_jogador_por_id(dados_partida['id_jogador1'])
        jogador2 = self.__controlador_principal.pega_jogador_por_id(dados_partida['id_jogador2'])
        mapa = self.__controlador_principal.pega_mapa_por_tamanho(dados_partida['mapa'])
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
            self.__controlador_principal.mostra_mapa(partida.mapa.tabuleiro)
            posicao = self.__tela_partida.faz_jogada(num_jogada, jogador_vez.nome)
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
                if jogador1.total_pontos > jogador2.total_pontos:
                    partida.vencedor = jogador1
                    jogador1.adiciona_vitoria()
                    self.__tela_partida.lista_vencedor(partida.vencedor)
                elif jogador2.total_pontos > jogador1.total_pontos:
                    partida.vencedor = jogador2
                    jogador2.adiciona_vitoria()
                    self.__tela_partida.lista_vencedor(partida.vencedor)
                else:
                    partida.vencedor = jogador_vez
                    jogador_vez.adiciona_vitoria()
                    self.__tela_partida.lista_vencedor(partida.vencedor)
                break

    def lista_partida(self):
        dados_partida = []
        for partida in self.__partidas:
            dados_partida.append({'id': partida.id,
                             'jogadores': partida.jogadores,
                             'mapa': partida.mapa.id,
                             'jogadas':len(partida.jogadas),
                             'qtd_acertos':len(partida.acertos),
                             'qtd_jogadas': partida.total_jogadas,
                             'vencedor': partida.vencedor.nome})
        self.__tela_partida.lista_partida(dados_partida)

    def retornar(self):
        self.__controlador_principal.inicia()

    def mostra_tela_opcoes(self):
        opcoes = {1: self.inicia_partida,
                  2: self.lista_partida,
                  0: self.retornar}
        while True:
            opcao = self.__tela_partida.mostra_opcoes()
            if opcao == 0:
                break
            opcoes[opcao]()
