
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

    def pega_dados_mapa(self):
        print("*" * 20)
        print("Cadastro de Mapa")
        print("*" * 20)
        tamanho_x = int(input("Determine a quantidade de linhas do seu mapa: "))
        tamanho_y = int(input("Determine a quantidade de colunas do seu mapa: "))
        return {"tamanho_x" : tamanho_x, "tamanho": tamanho_y}
