

class JogadorInvalidoException(Exception):
    def __init__(self):
        super().__init__('Jogadores inválidos')
