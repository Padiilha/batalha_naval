from dao.dao_partida import PartidaDAO
from modelo.jogada import Jogada
from modelo.partida import Partida
from visualizacao.tela_partida import TelaPartida


class ControladorPartida:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__partida_DAO = PartidaDAO()
        self.__tela_partida = TelaPartida()
        self.__id = self.__partida_DAO.tam_cache() + 1

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
        jogador1.adiciona_jogo()
        jogador2.adiciona_jogo()
        num_jogada = 1
        while True:
            if num_jogada % 2 == 1:
                jogador_vez = jogador1
            else:
                jogador_vez = jogador2
            self.__controlador_principal.mostra_mapa(partida.mapa.tabuleiro_para_jogadores)
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
                if jogador1.pontos_partida > jogador2.pontos_partida:
                    partida.vencedor = partida.jogadores[0]
                    jogador1.adiciona_vitoria()
                    self.__tela_partida.feedback(jogador1.nome + " ganhou a partida com "
                                                 + str(jogador1.pontos_partida) + " pontos!")
                    jogador1.zera_pontos_partida()
                    jogador2.zera_pontos_partida()
                    break
                elif jogador2.pontos_partida > jogador1.pontos_partida:
                    partida.vencedor = partida.jogadores[1]
                    jogador2.adiciona_vitoria()
                    self.__tela_partida.feedback(jogador2.nome + " ganhou a partida com "
                                                 + str(jogador2.pontos_partida) + " pontos!")
                    jogador1.zera_pontos_partida()
                    jogador2.zera_pontos_partida()
                    break
                else:
                    self.__tela_partida.feedback("Empate! " + str(jogador1.pontos_partida)
                                                 + " x " + str(jogador2.pontos_partida))
                    jogador1.zera_pontos_partida()
                    jogador2.zera_pontos_partida()
                    partida.vencedor.nome = "Empate"
                    break
                break
        self.__partida_DAO.add(partida)
        self.__controlador_principal.atualiza_jogadores()

    def lista_partida(self):
        for partida in self.__partida_DAO.get_all():
            dados_partida = [partida.id,
                             partida.jogadores[0].nome,
                             partida.jogadores[1].nome,
                             partida.mapa.id,
                             partida.total_jogadas,
                             len(partida.acertos),
                             partida.vencedor.nome]
            self.__tela_partida.lista_partida(dados_partida)

    def mostra_tela_opcoes(self):
        opcoes = {1: self.inicia_partida,
                  2: self.lista_partida}
        while True:
            opcao = self.__tela_partida.mostra_opcoes()
            if opcao == 0:
                break
            opcoes[opcao]()
