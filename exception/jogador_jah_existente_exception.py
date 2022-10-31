

class JogadorJahExistenteException(Exception):
    def __init__(self):
        super().__init__('Jogador já existente!')