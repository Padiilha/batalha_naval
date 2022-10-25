import random

from modelo.mapa import Mapa
from modelo.navio import TipoNavio, Navio
from visualizacao.tela_mapa import TelaMapa


class ControladorMapa:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__mapas = []
        self.__tela_mapa = TelaMapa()

    def inclui_mapa(self):
        dados = self.__tela_mapa.pega_dados_mapas()
        mapa = Mapa(dados["tamanho_x"],
                    dados["tamanho_y"])

        if not self.ja_existe_mapa(mapa['tamanho_x'], mapa["tamanho_y"]):
            i = 0
            tipos_navios = [TipoNavio.SUBMARINO, TipoNavio.FRAGATA, TipoNavio.NAVIOS_TANQUES, TipoNavio.PORTA_AVIOES]
            while len(mapa.navios) < 4:
                tipo_sorteado = random.choice(tipos_navios)
                navio = Navio(id, tipo_sorteado)
                mapa.navios.append(navio)
                i += 1
            self.__mapas.append(mapa)

    def ja_existe_mapa(self, tamanho_x, tamanho_y):
        for mapa in self.__mapas:
            if mapa.tamanho_x == tamanho_x and mapa.tamanho_y == tamanho_y:
                return True
            else:
                return False

    def lista_mapas(self):
        for mapa in self.__mapas:
            dados_mapa = {"tamanho_x": mapa.tamanho_x, "tamanho_y": mapa.tamanho_y}
            self.__tela_mapa.mostra_mapas(dados_mapa)

    def altera_mapas(self):
        dados_mapa = self.__tela_mapa.pega_dados_altera_mapa()
        novo_mapa = Mapa(dados_mapa["tamanho_x"],
                         dados_mapa["tamanho_y"])
        for mapa in self.__mapas:
            if mapa.id == dados_mapa["id"]:
                self.__mapas.remove()

    def remove_mapa(self):
        dados_mapa = self.__tela_mapa.pega_dados_e_deleta_mapa()
        for mapa in self.__mapas:
            if mapa.id == dados_mapa.id:
                self.__mapas.remove(mapa)

    def inclui_navio(self, mapa, tipo):


    def lista_navios(self):
        id_mapa_escolhido = self.__tela_mapa.escolhe_mapa_contem_navios()
        for mapa in self.__mapas:
            if mapa.id == id_mapa_escolhido['id']:
                for navio_no_mapa in mapa.navios:
                    dados_navio = {"tamanho_navio": navio_no_mapa.tipo.value, "tipo": navio_no_mapa.tipo.name}
                    self.__tela_mapa.mostra_navios(dados_navio)

    def mostra_tela_opcoes(self):
        opcoes = {
            1: self.inclui_mapa,
            2: self.lista_mapas,
            3: self.altera_mapas,
            4: self.remove_mapa,
            5: self.inclui_navio,
            6: self.lista_navios,
        }
        while True:
            opcao = self.__tela_mapa.mostrar_opcoes()
            if opcao == 0:
                break
            opcoes[opcao]()