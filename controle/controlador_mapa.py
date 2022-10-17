from modelo.mapa import Mapa
from visualizacao.tela_mapa import TelaMapa

class ControladorMapa:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__mapas = []
        self.__tela_mapa = TelaMapa()


    def inclui_mapa(self):
        dados = self.__tela_mapa.pega_dados_mapa()
        mapa = Mapa(dados["tamanho_x"],
                    dados["tamanho_y"])
        if not self.ja_existe_mapa(mapa.tamanho_x, mapa.tamanho_y):
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
        pass

    def remove_mapa(self):
        dados_mapa = self.__tela_mapa.pega_dados_e_deleta_mapa()


    def inclui_navio(self, tipo, tamanho):
        pass

    def

    def mostra_tela_opcoes(self):
        opcoes = {
            1: self.inclui_mapa,
            2: self.lista_mapas,
            3: self.altera_mapas,
            4: self.remove_mapa
        }
        while True:
            opcao = self.__tela_mapa.mostrar_opcoes()
            if opcao == 0:
                break
            opcoes[opcao]()