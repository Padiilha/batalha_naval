

import PySimpleGUI as sg

class TelaPartida:
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
      [sg.Text('-------- PARTIDA ----------', font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio('Começar Partida ', "RD1", key='1')],
      [sg.Radio('Histórico de Partidas', "RD1", key='2')],
      [sg.Radio('Voltar', "RD1", key='0')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema de livros').Layout(layout)

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'
  def inicia_partida(self):
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text('-------- COMEÇAR PARTIDA ----------', font=("Helvica", 25))],
      [sg.Text('ID do Jogador 1:', size=(15, 1)), sg.InputText('', key='jogador_1')],
      [sg.Text('ID do Jogador 2:', size=(15, 1)), sg.InputText('', key='jogador_2')],
      [sg.Text('Tamanho do Mapa:', size=(15, 1)), sg.InputCombo(('Pequeno', 'Medio', 'Grande'), size=(20, 3), key='mapa')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]

    self.__window = sg.Window('Batalha Naval').Layout(layout)

    button, values = self.open()
    id_jogador1 = int(values['jogador_1'])
    id_jogador2 = int(values['jogador_2'])
    mapa = values['mapa'].upper()
    self.close()
    return {'id_jogador1': id_jogador1, 'id_jogador2': id_jogador2, 'mapa': mapa}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def lista_partida(self, dados_partida):
    string_todas_partidas = ""
    for dado in dados_partida:
      string_todas_partidas = string_todas_partidas + "PARTIDA -- " + str(dado['id']) + '\n'
      string_todas_partidas = string_todas_partidas + f"Jogadores: {dado['jogadores'][0].nome}, {dado['jogadores'][1].nome} " + '\n'
      string_todas_partidas = string_todas_partidas + "Mapa: " + str(dado['mapa']) + '\n'
      string_todas_partidas = string_todas_partidas + "Jogadas: " + str(dado['jogadas']) + '\n'
      string_todas_partidas = string_todas_partidas + "Quantidade de Acertos: " + str(dado['qtd_acertos']) + '\n'
      string_todas_partidas = string_todas_partidas + "Quantidade de Jogadas: " + str(dado['qtd_jogadas']) + '\n'
      string_todas_partidas = string_todas_partidas + "Vencedor: " + str(dado['vencedor']) + '\n\n'

    sg.Popup('-------- LISTA DE PARTIDAS ----------', string_todas_partidas)

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def faz_jogada(self, num_jogada, jogador):
    sg.ChangeLookAndFeel('DarkTeal4')
    layout = [
      [sg.Text(f'-------- JOGADA ---------- {str(num_jogada)} - {jogador}', font=("Helvica", 25))],
      [sg.Text('Digite as coordenadas que deseja atacar!', font=("Helvica", 15))],
      [sg.Text('Linha :', size=(15, 1)), sg.InputText('', key='linha')],
      [sg.Text('Coluna :', size=(15, 1)), sg.InputText('', key='coluna')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Jogada').Layout(layout)

    button, values = self.open()
    linha = int(values['linha'])
    coluna = int(values['coluna'])
    posicao = (linha, coluna)
    self.close()
    return posicao

  def lista_vencedor(self, jogador_vencedor):
    self.mostra_mensagem(f'PARTIDA FINALIZADA \n\nVENCEDOR DA PARTIDA - {jogador_vencedor.nome}')

  def mostra_mensagem(self, msg):
    sg.popup("", msg)

  def close(self):
    self.__window.Close()

  def open(self):
    button, values = self.__window.Read()
    return button, values

