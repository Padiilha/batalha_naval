

class TelaPartida:

    def mostra_opcoes(self) -> int:
        print("*" * 50)
        print("Partida")
        print("*" * 50)
        print("1 - Começar Partida")
        print("2 - Histórico de Partidas")
        print("3 - Alterar Partida (só não vai alterar o vencedor, né)")
        print("4 - Remover Partida (ih alá, perdeu e não quer mostrar)")
        print("0 - Voltar")
        opcao = int(input("Selecione o que deseja realizar: "))
        return opcao

    def pega_dados(self):
        pass

    def lista_partidas(self):
        pass