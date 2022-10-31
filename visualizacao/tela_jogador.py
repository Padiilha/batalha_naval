

class TelaJogador:

    def mostra_opcoes(self) -> int:
        print("*" * 50)
        print(" " * 21 + "JOGADOR")
        print("*" * 50)
        print("1 - Cadastrar Jogador")
        print("2 - Lista de Jogadores")
        print("3 - Atualizar Jogador")
        print("4 - Remover Jogador")
        print("0 - Voltar")
        opcao = int(input("Selecione o que deseja realizar: "))
        return opcao

    def incluir_jogador(self) -> str:
        print("*" * 50)
        print(" " * 16 + "CADASTRO DE JOGADOR")
        print("*" * 50)
        nome = input("Nome do jogador: ")
        return nome

    def lista_jogadores(self, dados_jogador: list):
        print("*" * 50)
        print(" " * 20 + str(dados_jogador[1]))
        print("*" * 50)
        print("ID: " + str(dados_jogador[0]))
        print("Total de Pontos: " + str(dados_jogador[2]))
        print("Posição no Ranking: " + str(dados_jogador[3]))
        print("Quantidade de Jogos: " + str(dados_jogador[4]))
        print("Quantidade de Vitórias: " + str(dados_jogador[5]))

    def altera_jogador(self) -> list:
        print("*" * 50)
        print(" " * 17 + "ALTERAR JOGADOR")
        print("*" * 50)
        id = int(input("ID do jogador: "))
        nome = input("Nome do jogador: ")
        dados_jogador = [id, nome]
        return dados_jogador

    def remove_jogador(self) -> int:
        print("*" * 50)
        print(" " * 17 + "REMOVER JOGADOR")
        print("*" * 50)
        id = int(input("ID do jogador: "))
        return id

    def feedback(self, mensagem: str):
        print(mensagem)
