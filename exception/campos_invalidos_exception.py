

class CamposInvalidosException(Exception):
    def __init__(self):
        super().__init__('Campos inválidos foram preenchidos!')
