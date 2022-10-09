

class TelaPrincipal:

    def mostra_tela_inicial(self):
        print("*" * 50)
        print(" " * 18 + "BATALHA NAVAL")
        print("*" * 50)
        print("")
        print("1 - Mapas")
        print("2 - Partidas")
        print("3 - Jogadas")
        print("4 - Jogadores")
        print("0 - Sair")

        opcao = int(input("Escolha a opção: "))

        return opcao
