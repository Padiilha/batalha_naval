import sys

from visualizacao.tela_principal import TelaPrincipal
from controle.controlador_partida import ControladorPartida
from controle.controlador_mapa import ControladorMapa
from controle.controlador_jogador import ControladorJogador


class ControladorPrincipal:
    def __init__(self):
        self.__tela_principal = TelaPrincipal()
        self.__controlador_mapa = ControladorMapa(self)
        self.__controlador_partida = ControladorPartida(self)
        self.__controlador_jogador = ControladorJogador(self)

    def inicia(self):
        opcoes = {1: self.inicia_mapa,
                  2: self.inicia_partida,
                  3: self.inicia_jogador,
                  0: self.encerra}

        while True:
            opcao = self.__tela_principal.mostra_tela_inicial()
            opcoes[opcao]()

    def inicia_mapa(self):
        self.__controlador_mapa.mostra_tela_opcoes()

    def inicia_partida(self):
        self.__controlador_partida.mostra_tela_opcoes()

    def inicia_jogador(self):
        self.__controlador_jogador.mostra_tela_opcoes()

    def pega_mapa_por_tamanho(self, tamanho: str):
        mapa = self.__controlador_mapa.cria_e_inclui_mapa(tamanho)
        return mapa

    def pega_jogador_por_id(self, id: int):
        jogador = self.__controlador_jogador.pega_jogador_por_id(id)
        return jogador

    def mostra_mapa(self, matriz):
        self.__controlador_mapa.mostra_matriz(matriz)

    def encerra(self):
        sys.exit()
