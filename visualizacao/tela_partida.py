

class TelaPartida:

    def mostra_opcoes(self) -> int:
        print("*" * 50)
        print(" " * 21 + "PARTIDA")
        print("*" * 50)
        print("1 - Começar Partida")
        print("2 - Histórico de Partidas")
        print("0 - Voltar")
        opcao = int(input("Selecione o que deseja realizar: "))
        return opcao

    def inicia_partida(self) -> list:
        print("*" * 50)
        print(" " * 17 + "COMEÇAR PARTIDA")
        print("*" * 50)
        id_jogador1 = int(input("ID do jogador 1: "))
        id_jogador2 = int(input("ID do jogador 2: "))
        tam_mapa = str(input("Tamanho do mapa desejado (P, M ou G): ")).upper()
        dados_partida = [id_jogador1, id_jogador2, tam_mapa]
        return dados_partida

    def lista_partida(self, dados_partida: list):
        print("*" * 50)
        print(" " * 20 + "PARTIDA " + str(dados_partida[0]))
        print("*" * 50)
        print("Jogadores: " + str(dados_partida[1]) + ", " + str(dados_partida[2]))
        print("Mapa: " + str(dados_partida[3]))
        print("Quatidade de Jogadas: " + str(dados_partida[4]))
        print("Quantidade de Acertos: " + str(dados_partida[5]))
        print("Vencedor: " + str(dados_partida[6]))

    def faz_jogada(self, num_jogada, jogador) -> tuple:
        print("*" * 50)
        print(" " * 15 + "JOGADA " + str(num_jogada) + " - " + jogador)
        print("*" * 50)
        linha = int(input("Digite a linha que deseja acertar: "))
        coluna = int(input("Digite a coluna que deseja acertar: "))
        posicao = (linha, coluna)
        return posicao

    def feedback(self, mensagem: str):
        print(mensagem)
