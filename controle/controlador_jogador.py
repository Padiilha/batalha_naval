from dao.dao_jogador import JogadorDAO
from exception.campos_invalidos_exception import CamposInvalidosException
from exception.jogador_invalido_exception import JogadorInvalidoException
from modelo.jogador import Jogador
from visualizacao.tela_jogador import TelaJogador


class ControladorJogador:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__jogador_dao = JogadorDAO()
        self.__tela_jogador = TelaJogador()
        self.__id = self.__jogador_dao.tam_cache() + 1

    def inclui_jogador(self):
        jogador_novo = self.__tela_jogador.incluir_jogador()
        if isinstance(jogador_novo['nome'], str):
            jogador = Jogador(self.__id, jogador_novo['nome'])
            self.__id += 1
            self.__jogador_dao.add(jogador)
            self.__tela_jogador.mostra_mensagem(jogador.nome + ' adicionado! ID ' + str(jogador.id))
        else:
            raise CamposInvalidosException

    def lista_jogador(self):
        dados_jogadores = []
        for jogador in self.__jogador_dao.get_all():
            dados_jogadores.append({"nome": jogador.nome, "id": jogador.id, "total_pontos": jogador.total_pontos, "ranking": jogador.posicao_ranking, "qtd_jogos": jogador.qtd_jogos, "vitorias": jogador.qtd_vitorias})
        self.__tela_jogador.lista_jogadores(dados_jogadores)

    def altera_jogador(self):
        dados_jogador = self.__tela_jogador.altera_jogador()
        if isinstance(dados_jogador['id'], int) and\
                isinstance(dados_jogador['nome'], str):
            for jogador in self.__jogador_dao.get_all():
                if jogador.id == dados_jogador['id']:
                    jogador.nome = dados_jogador['nome']
                    self.__tela_jogador.mostra_mensagem('Nome do jogador ' +
                                                 str(jogador.id) +
                                                 ' foi atualziado com sucesso! Novo nome : ' +
                                                 jogador.nome)
        else:
            raise CamposInvalidosException

    def remove_jogador(self):
        try:
            jogador = self.__tela_jogador.remove_jogador()
            if isinstance(jogador['id'], int):
                self.__jogador_dao.remove(jogador['id'])
                self.__tela_jogador.mostra_mensagem('Jogador ' + str(jogador['id']) + ' removido')
        except:
            self.__tela_jogador.mostra_mensagem('ID Inválido! Digite um Valor válido')
            self.__tela_jogador.close()

    def retornar(self):
        self.__controlador_principal.inicia()

    def mostra_tela_opcoes(self):
        opcoes = {1: self.inclui_jogador,
                  2: self.lista_jogador,
                  3: self.altera_jogador,
                  4: self.remove_jogador,
                  0: self.retornar}
        continua = True
        while continua:
            opcoes[self.__tela_jogador.mostra_opcoes()]()

    def pega_jogador_por_id(self, id: int) -> Jogador:
        for jogador in self.__jogador_dao.get_all():
            if jogador.id == id:
                return jogador
        raise JogadorInvalidoException

    def jogadorDAO(self):
        return self.__jogador_dao
