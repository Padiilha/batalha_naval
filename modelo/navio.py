from enum import Enum

class TipoNavio(Enum):
    SUBMARINO = 2
    FRAGATA = 3
    NAVIOS_TANQUES = 4
    PORTA_AVIOES = 5

class Navio:
    def __init__(self, id, tipo: TipoNavio):
        self.id = id
        self.tipo = tipo

