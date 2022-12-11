from dao.abstract_dao import DAO
from modelo.jogada import Jogada


class JogadaDAO(DAO):
    def __init__(self):
        super().__init__('jogada.pkl')

    def add(self, jogada: Jogada):
        if jogada is not None \
                and isinstance(jogada, Jogada) \
                and isinstance(jogada.num_jogada, int):
            super().add(jogada.num_jogada, jogada)
    
    def get(self, key: int):
        if isinstance(key, int):
            super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            super().remove(key)
