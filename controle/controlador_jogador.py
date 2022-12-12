from dao.dao_jogador import JogadorDAO
from exception.campos_invalidos_exception import CamposInvalidosException
from exception.jogador_invalido_exception import JogadorInvalidoException
from modelo.jogador import Jogador
from visualizacao.tela_jogador import TelaJogador


class ControladorJogador:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__jogador_DAO = JogadorDAO()
        self.__tela_jogador = TelaJogador()
        self.__id = self.__jogador_DAO.tam_cache() + 1

    def inclui_jogador(self):
        nome = self.__tela_jogador.incluir_jogador()
        if isinstance(nome, str):
            jogador = Jogador(self.__id, nome)
            self.__id += 1
            self.__jogador_DAO.add(jogador)
            self.__tela_jogador.feedback(jogador.nome + ' adicionado! ID ' + str(jogador.id))
        else:
            raise CamposInvalidosException

    def lista_jogador(self):
        for jogador in self.__jogador_DAO.get_all():
            dados_jogador = [jogador.id,
                             jogador.nome,
                             jogador.total_pontos,
                             jogador.posicao_ranking,
                             jogador.qtd_jogos,
                             jogador.qtd_vitorias]
            self.__tela_jogador.lista_jogadores(dados_jogador)

    def altera_jogador(self):
        dados_jogador = self.__tela_jogador.altera_jogador()
        if isinstance(dados_jogador[0], int) and\
                isinstance(dados_jogador[1], str):
            for jogador in self.__jogador_DAO.get_all():
                if jogador.id == dados_jogador[0]:
                    jogador.nome = dados_jogador[1]
                    self.__tela_jogador.feedback('Nome do jogador ' +
                                                 str(jogador.id) +
                                                 'atualziado: ' +
                                                 jogador.nome)
                    self.__jogador_DAO.update()
        else:
            raise CamposInvalidosException

    def remove_jogador(self):
        id = self.__tela_jogador.remove_jogador()
        if isinstance(id, int):
            self.__jogador_DAO.remove(id)
            self.__tela_jogador.feedback('Jogador ' + str(id) + ' removido')
        else:
            raise CamposInvalidosException

    def mostra_tela_opcoes(self) -> int:
        opcoes = {1: self.inclui_jogador,
                  2: self.lista_jogador,
                  3: self.altera_jogador,
                  4: self.remove_jogador}
        while True:
            opcao = self.__tela_jogador.mostra_opcoes()
            if opcao == 0:
                break
            opcoes[opcao]()

    def pega_jogador_por_id(self, id: int) -> Jogador:
        for jogador in self.__jogador_DAO.get_all():
            if jogador.id == id:
                return jogador
        raise JogadorInvalidoException

    def jogadorDAO(self):
        return self.__jogador_DAO
