
class TelaMapa:

    def mostrar_opcoes(self):
        print("*" * 20)
        print("MAPAS")
        print("*" * 20)
        print("1 - Incluir Mapa")
        print("2 - Listar Mapa")
        print("3 - Alterar Mapa")
        print("4 - Excluir Mapa")
        print("0 - Voltar")
        opcao = int(input("Selecione o que deseja realizar: "))
        return opcao

    def pega_dados_mapas(self):
        print("*" * 20)
        print("Cadastro de Mapa")
        print("*" * 20)
        tamanho_x = int(input("Determine a quantidade de linhas do seu mapa: "))
        tamanho_y = int(input("Determine a quantidade de colunas do seu mapa: "))
        return {"tamanho_x" : tamanho_x, "tamanho_y": tamanho_y}

    def mostra_mapas(self, dados_mapa):
        print("MAPA")
        print(f"Tamanho X:" {dados_mapa['tamanho_x']})
        print(f"Tamanho Y:" {dados_mapa['tamanho_y']})
        print("")

    def pega_dados_altera_mapa(self):
        print("*" * 20)
        print("Alteração de Mapa")
        print("*" * 20)
        id_mapa = int(input("Insira o ID do mapa que deseja atualizar: "))
        tamanho_x = int(input("Qual o tamanho X do seu novo mapa: "))
        tamanho_y = int(input("Qual o tamanho Y do seu novo mapa: "))
        return {"id" : id_mapa, tamanho_x": tamanho_x, "tamanho_y": tamanho_y}

    def pega_dados_deleta_mapa(self):
        print("*" * 20)
        print("Remoção de Mapa")
        print("*" * 20)
        id_mapa = int(input("Insira o ID do mapa que deseja remover: "))
        return {"id" : id_mapa}

'''NAVIOS ABAIXO'''
    def pega_dados_navio(self):
        print("*" * 20)
        print("Cadastro de Navios")
        print("*" * 20)
        tamanho_navio = int(input("Determine o tamanho que seu navio irá ocupar: "))
        tipo_navio = int(input("Determine o tipo que seu navio irá ocupar: "))
        return {"tamanho_navio" : tamanho_navio, "tipo_navio": tipo_navio}

    def mostra_navio(self, dados_navio):
        print("*" * 20)
        print("NAVIO")
        print("*" * 20)
        print(f"Tamanho do Navio:"{dados_navio['tamanho_navio']})
        print(f"Tipo do Navio:"{dados_navio['tipo_navio']})

    def pega_dados_altera_navio(self):
        print("*" * 20)
        print("Alteração de Navio")
        print("*" * 20)
        tamanho_navio = int(input("Determine o tamanho que seu novo navio irá ocupar: "))
        tipo_navio = int(input("Determine o tipo do seu novo navio: "))
        return {"tamanho_navio" : tamanho_navio, "tipo_navio": tipo_navio}

    def pega_dados_deleta_navio(self):
        print("*" * 20)
        print("Remoção de Navio")
        print("*" * 20)
        id_navio = int(input("Insira o ID do Navio que deseja remover: "))
        return {"id" : id_navio}