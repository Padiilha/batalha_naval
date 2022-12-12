## Excluir
class TelaMapa:

    def mostrar_opcoes(self):
        print("*" * 20)
        print("MAPAS")
        print("*" * 20)
        print("1 - Incluir Mapa")
        print("2 - Listar Mapa")
        print("3 - Alterar Mapa")
        print("4 - Excluir Mapa")
        print("5 - Listar Navios")
        print("0 - Voltar")
        opcao = int(input("Selecione o que deseja realizar: "))
        return opcao

    def pega_dados_mapas(self):
        print("*" * 20)
        print("Cadastro de Mapa")
        print("*" * 20)
        tamanho_mapa = str(input("Escolha o tamanho do Mapa que deseja jogar, Pequeno(P), Médio(M) ou Grande(G): "))
        return {"tamanho_mapa": tamanho_mapa}

    def mostra_mapas(self, dados_mapa):
        print("MAPA")
        print(f"Tamanho X: {dados_mapa['tamanho_x']}")
        print(f"Tamanho Y: {dados_mapa['tamanho_y']}")
        print("")

    def pega_dados_altera_mapa(self):
        print("*" * 20)
        print("Alteração de Mapa")
        print("*" * 20)
        id_mapa = int(input("Insira o ID do mapa que deseja atualizar: "))
        tamanho_x = int(input("Qual o tamanho X do seu novo mapa: "))
        tamanho_y = int(input("Qual o tamanho Y do seu novo mapa: "))
        return {"id" : id_mapa, "tamanho_x" : tamanho_x, "tamanho_y": tamanho_y}

    def pega_dados_deleta_mapa(self):
        print("*" * 20)
        print("Remoção de Mapa")
        print("*" * 20)
        id_mapa = int(input("Insira o ID do mapa que deseja remover: "))
        return {"id" : id_mapa}

    def escolhe_mapa_contem_navios(self):
        print("*"*20)
        id_mapa_escolhido = int(input("Digite o ID do Mapa que deseja ver os navios: "))
        return {"id" : id_mapa_escolhido}

    def mostra_navios(self, dados_navio):
        print("*" * 20)
        print("NAVIOS NO MAPA")
        print("*" * 20)
        print(f"Tamanho do Navio: {dados_navio['tamanho_navio']}")
        print(f"Tipo do Navio:{dados_navio['tipo']}")

