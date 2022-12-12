

import PySimpleGUI as sg

class TelaJogador:
  def __init__(self):
    self.__window = None
    self.init_opcoes()

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_opcoes(self):
    self.init_opcoes()
    button, values = self.open()
    if values['1']:
      opcao = 1
    if values['2']:
      opcao = 2
    if values['3']:
      opcao = 3
    if values['4']:
      opcao = 4
    # cobre os casos de Retornar, fechar janela, ou clicar cancelar
    #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
    if values['0'] or button in (None, 'Cancelar'):
      opcao = 0
    self.close()
    return opcao

  def init_opcoes(self):
    #sg.theme_previewer()
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- JOGADOR ----------', font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio('Cadastrar Jogador ', "RD1", key='1')],
      [sg.Radio('Listar Jogadores', "RD1", key='2')],
      [sg.Radio('Atualizar  Jogador', "RD1", key='3')],
      [sg.Radio('Remover Jogador', "RD1", key='4')],
      [sg.Radio('Voltar', "RD1", key='0')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Batalha Naval').Layout(layout)

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'
  def incluir_jogador(self):
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- DADOS JOGADOR ----------', font=("Helvica", 25))],
      [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Batalha Naval - Cadastro').Layout(layout)

    button, values = self.open()
    nome = values['nome']

    self.close()
    return {"nome": nome}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def lista_jogadores(self, dados_jogador):
    string_todos_jogadores = ""
    for dado in dados_jogador:
      string_todos_jogadores = string_todos_jogadores + "Nome do Jogador: " + dado['nome'] + '\n'
      string_todos_jogadores = string_todos_jogadores + "ID do Jogador: " + str(dado['id']) + '\n'
      string_todos_jogadores = string_todos_jogadores + "Total de Pontos: " + str(dado['total_pontos']) + '\n'
      string_todos_jogadores = string_todos_jogadores + "Posição do Ranking: " + str(dado['ranking']) + '\n'
      string_todos_jogadores = string_todos_jogadores + "Quantidade de Jogos: " + str(dado['qtd_jogos']) + '\n'
      string_todos_jogadores = string_todos_jogadores + "Quantidade de Vitórias: " + str(dado['vitorias']) + '\n\n'

    sg.Popup('-------- LISTA DE JOGADORES ----------', string_todos_jogadores)

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def altera_jogador(self):
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- ALTERAR JOGADOR ----------', font=("Helvica", 25))],
      [sg.Text('Digite o ID do jogador que deseja alterar:', font=("Helvica", 15))],
      [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
      [sg.Text('Novo Nome:', size=(15, 1)), sg.InputText('', key='nome')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Batalha Naval - Alterar Jogador').Layout(layout)

    button, values = self.open()
    id = int(values['id'])
    nome = values['nome']
    self.close()
    return {'id': id, 'nome': nome}

  def remove_jogador(self):
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- REMOVE JOGADOR ----------', font=("Helvica", 25))],
      [sg.Text('Digite o ID do jogador que deseja remover:', font=("Helvica", 15))],
      [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Batalha Naval - Removendo Jogador').Layout(layout)

    button, values = self.open()
    id = int(values['id'])
    self.close()
    return {'id': id}

  def mostra_mensagem(self, msg):
    sg.popup("", msg)

  def close(self):
    self.__window.Close()

  def open(self):
    button, values = self.__window.Read()
    return button, values

  def feedback(self, mensagem: str):
    print(mensagem)
