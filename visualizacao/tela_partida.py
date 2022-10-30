

class TelaPartida:

    def mostra_opcoes(self) -> int:
        print("*" * 50)
        print("Partida")
        print("*" * 50)
        print("1 - Começar Partida")
        print("2 - Histórico de Partidas")
        print("0 - Voltar")
        opcao = int(input("Selecione o que deseja realizar: "))
        return opcao

    def inicia_partida(self) -> list:
        print("*" * 50)
        print("Começar Partida")
        print("*" * 50)
        id_jogador1 = int(input("ID do jogador 1: "))
        id_jogador2 = int(input("ID do jogador 2: "))
        id_mapa = int(input("Tamanho do mapa desejado: "))
        dados_partida = [id_jogador1, id_jogador2, id_mapa]
        return dados_partida

    def lista_partida(self, dados_partida: list):
        print("*" * 50)
        print("***** Partida " + dados_partida[0] + " *****")
        print("Jogadores: " + dados_partida[1])
        print("Mapa: " + dados_partida[2])
        print("Jogadas: " + dados_partida[3])
        print("Quantidade de Acertos: " + dados_partida[4])
        print("Quantidade de Jogadas: " + dados_partida[5])
        print("Vencedor: " + dados_partida[6])
        print("*" * 50)

    def faz_jogada(self, num_jogada) -> tuple:
        print("*" * 50)
        print("Jogada " + num_jogada)
        print("*" * 50)
        linha = int(input("Digite a linha que deseja acertar: "))
        coluna = int(input("Digite a coluna que deseja acertar: "))
        posicao = (linha, coluna)
        return posicao
