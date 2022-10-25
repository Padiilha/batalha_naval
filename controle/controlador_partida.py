from controle.controlador_principal import ControladorPrincipal
from exception.campos_invalidos_exception import CamposInvalidosException
from exception.jogador_invalido_exception import JogadorInvalidoException
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

    def inicia_partida(self,
                       jogador1: Jogador,
                       jogador2: Jogador,
                       mapa: Mapa):
        if isinstance(jogador1, Jogador) and \
                isinstance(jogador2, Jogador) and \
                isinstance(mapa, Mapa):
            partida = Partida(self.__id)
            self.__id += 1
            partida.adiciona_jogadores(jogador1, jogador2)
            partida.mapa = mapa
            while True:
                jogada = ControladorPrincipal.inicia_jogada(mapa)
                partida.adiciona_jogada(jogada.posicao)
                partida.conta_jogada()
                if jogada.acerto:
                    partida.adiciona_acerto(jogada.acerto)
                if jogada.vencedor is not None:
                    partida.vencedor(jogada.vencedor)
                    break
        else:
            raise JogadorInvalidoException

    def lista_partida(self) -> list:
        for partida in self.__partidas:
            dados_partida = [partida.id,
                             partida.jogadores,
                             partida.mapa,
                             partida.jogadas,
                             partida.acertos,
                             partida.total_jogadas,
                             partida.vencedor]
            return dados_partida

    def altera_partida(self):
        pass

    def remove_partida(self, id: int):
        if isinstance(id, int):
            self.__partidas.remove(id)
        else:
            CamposInvalidosException

    def mostra_tela_opcoes(self):
        opcoes = {1: self.inicia_partida,
                  2: self.lista_partida,
                  3: self.altera_partida,
                  4: self.remove_partida}
        while True:
            opcao = self.__tela_partida.mostra_opcoes()
            if opcao == 0:
                break
            opcoes[opcao]()
