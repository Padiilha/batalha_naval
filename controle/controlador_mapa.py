import random

from modelo.mapa import Mapa
from modelo.navio import TipoNavio, Navio
from visualizacao.tela_mapa import TelaMapa


class ControladorMapa:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__mapas = []
        self.__tela_mapa = TelaMapa()
        self.__id = 1

    def cria_e_inclui_mapa(self, tamanho_mapa):
        self.__id += 1
        if tamanho_mapa == "P":
            mapa = Mapa(self.__id, self.cria_mapa(6, 6), self.cria_mapa(6, 6), 6, 6, 4)

            id_navios = 1
            tipos_navios = [TipoNavio.SUBMARINO, TipoNavio.FRAGATA, TipoNavio.NAVIOS_TANQUES, TipoNavio.PORTA_AVIOES]
            while len(mapa.navios) < 4:
                id_navios += 1
                tipo_sorteado = random.choice(tipos_navios)
                navio = Navio(id_navios, tipo_sorteado)
                self.incluir_mapa(mapa.tabuleiro, navio.tipo.value, mapa.linhas, mapa.colunas)
                mapa.navios.append(navio)

            self.__mapas.append(mapa)
            return mapa

        elif tamanho_mapa == "M":
            mapa = Mapa(self.__id, self.cria_mapa(8, 8), self.cria_mapa(8, 8), 8, 8, 5)

            id_navios = 1
            tipos_navios = [TipoNavio.SUBMARINO, TipoNavio.FRAGATA, TipoNavio.NAVIOS_TANQUES, TipoNavio.PORTA_AVIOES]
            while len(mapa.navios) < 5:
                id_navios += 1
                tipo_sorteado = random.choice(tipos_navios)
                navio = Navio(id_navios, tipo_sorteado)
                self.incluir_mapa(mapa.tabuleiro, navio.tipo.value, mapa.linhas, mapa.colunas)
                mapa.navios.append(navio)

            self.__mapas.append(mapa)
            return mapa


        elif tamanho_mapa == "G":
            mapa = Mapa(self.__id, self.cria_mapa(10, 10), self.cria_mapa(10, 10), 10, 10, 6)

            id_navios = 1
            tipos_navios = [TipoNavio.SUBMARINO, TipoNavio.FRAGATA, TipoNavio.NAVIOS_TANQUES, TipoNavio.PORTA_AVIOES]
            while len(mapa.navios) < 6:
                id_navios += 1
                tipo_sorteado = random.choice(tipos_navios)
                navio = Navio(id_navios, tipo_sorteado)
                self.incluir_mapa(mapa.tabuleiro, navio.tipo.value, mapa.linhas, mapa.colunas)
                mapa.navios.append(navio)

            self.__mapas.append(mapa)
        return mapa

    def cria_mapa(self, linhas, colunas):
        mapa = []
        for i in range(linhas):
            linha = []
            for j in range(colunas):
                linha.append('~')
            mapa.append(linha)
        return mapa

    def mostra_matriz(self, mapa):
        letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M' 'N',
                       'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'v', 'W', 'X', 'Y', 'Z']
        print(' ', *letras[:len(mapa)])
        for index, line in enumerate(mapa):
            print(index, *line)

    def posiciona_navios(self, mapa, i, j, tamanho_navio):
        for posicao in range(tamanho_navio):
            if i >= len(mapa) or i < 0 or j + posicao >= len(mapa[0]) or j + posicao < 0 or not \
            mapa[i][j + posicao] == '~':
                return False

        for posicao in range(tamanho_navio):
            if tamanho_navio == 2:
                mapa[i][j + posicao] = 'S'
            elif tamanho_navio == 3:
                mapa[i][j + posicao] = 'F'
            elif tamanho_navio == 4:
                mapa[i][j + posicao] = 'N'
            elif tamanho_navio == 5:
                mapa[i][j + posicao] = 'P'
        return True

    def incluir_mapa(self, mapa, tamanho_navio, linhas_mapa, colunas_mapa):
        posicionou_certo = False
        while not posicionou_certo:
            linha = random.randrange(0, linhas_mapa)
            coluna = random.randrange(0, colunas_mapa)
            posicionou_certo = self.posiciona_navios(mapa, linha, coluna, tamanho_navio)

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
            5: self.lista_navios,
        }
        while True:
            opcao = self.__tela_mapa.mostrar_opcoes()
            if opcao == 0:
                break
            opcoes[opcao]()
