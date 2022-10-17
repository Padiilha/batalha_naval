

class TelaJogador:

    def mostra_opcoes(self) -> int:
        print("*" * 50)
        print("Jogador")
        print("*" * 50)
        print("1 - Cadastrar Jogador")
        print("2 - Lista de Jogadores")
        print("3 - Atualizar Jogador")
        print("4 - Remover Jogador")
        print("0 - Voltar")
        opcao = int(input("Selecione o que deseja realizar: "))
        return opcao

    def pega_dados(self):
        pass

    def lista_jogadores(self):
        pass
