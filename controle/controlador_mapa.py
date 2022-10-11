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
        self.__mapas.append(mapa)

    def lista_mapas(self):
        pass

    def altera_mapas(self):
        pass

    def remove_mapa(self):
        pass

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