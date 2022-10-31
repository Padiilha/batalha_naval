

class MapaInvalidoException(Exception):
    def __init__(self):
        super().__init__('Mapa Inválido')
