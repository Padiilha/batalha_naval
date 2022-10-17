import sys

from visualizacao.tela_principal import TelaPrincipal
from controle.controlador_partida import ControladorPartida
from controle.controlador_mapa import ControladorMapa


class ControladorPrincipal:

    def __init__(self):
        self.__tela_principal = TelaPrincipal()
        self.__controlador_mapa = ControladorMapa(self)
        self.__controlador_partida = ControladorPartida(self)
        '''self.__controlador_jogada = ControladorJogada(self)
        self.__controlador_jogador = ControladorJogador(self)'''

    def inicia(self):
        opcoes = {1: self.inicia_mapa,
                  2: self.inicia_partida,
                  3: self.inicia_jogada,
                  4: self.inicia_jogador,
                  0: self.encerra}

        while True:
            opcao = self.__tela_principal.mostra_tela_inicial()
            opcoes[opcao]()

    def inicia_mapa(self):
        pass

    def inicia_partida(self):
        pass

    def inicia_jogada(self):
        pass

    def inicia_jogador(self):
        pass

    def encerra(self):
        sys.exit()
