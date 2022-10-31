

class TelaPrincipal:

    def mostra_tela_inicial(self):
        print("*" * 50)
        print(" " * 18 + "BATALHA NAVAL")
        print("*" * 50)
        print("")
        print("1 - Partidas")
        print("2 - Jogadores")
        print("0 - Sair")

        opcao = int(input("Escolha a opção: "))

        return opcao
