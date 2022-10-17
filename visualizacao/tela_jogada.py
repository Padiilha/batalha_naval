

class TelaJogada:

    def mostra_opcoes(self) -> int:
        print("*" * 50)
        print("Jogada")
        print("*" * 50)
        print("1 - Fazer Jogada")
        print("2 - Histórico de Jogadas")
        print("3 - Alterar Jogada")
        print("4 - Remover Jogada")
        print("0 - Voltar")
        opcao = int(input("Selecione o que deseja realizar: "))
        return opcao

    def pega_dados(self):
        pass

    def lista_jogadas(self):
        pass