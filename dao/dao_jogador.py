from dao.abstract_dao import DAO
from modelo.jogador import Jogador


class JogadorDAO(DAO):
    def __init__(self):
        super().__init__('jogadores.pkl')

    def add(self, jogador: Jogador):
        if jogador is not None \
                and isinstance(jogador, Jogador) \
                and isinstance(jogador.id, int):
            super().add(jogador.id, jogador)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
