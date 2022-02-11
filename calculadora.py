import PySimpleGUI as sg 
from PySimpleGUI import *

class Calculadora:
    def __init__(self):
        self.resultado = ''
        # Configurando o layout
        self.layout = [[Txt(''  * 10)],
                  [Text('', size = (15, 1), font = ('bold', 18),
                        text_color = 'black', key = 'telinha', justification='right')],
                  [Txt(''  * 10)],
                  [sg.Button('7', size=(7,2)), sg.Button('8', size=(7,2)), sg.Button('9', size=(7,2)), sg.Button('/', size=(7,2))],
                  [sg.Button('4', size=(7,2)), sg.Button('5', size=(7,2)), sg.Button('6', size=(7,2)), sg.Button('x', size=(7,2))],
                  [sg.Button('1', size=(7,2)), sg.Button('2', size=(7,2)), sg.Button('3', size=(7,2)),sg.Button('-', size=(7,2))],
                  [sg.Button(',', size=(7,2)), sg.Button('0', size=(7,2)), sg.Button('+', size=(7,2)), sg.Button('=', size=(7,2))],
                  [sg.Button('c', size=(15,2)), sg.Button('<-', size=(18,2))],
                ]
        
    def Iniciar(self):
        
      # configurando o PySimpleGUI
        self.jeito = FlexForm('calculadora', default_button_element_size = (5, 2),
                        auto_size_buttons = False, grab_anywhere = False)

        # Abrindo a janela com as configurações setadas
        self.jeito.Layout(self.layout)

        # Variavel que guarda o resultado a ser mostrado
        self.resultado = ''

        # Laço Infinito principal
        while True:
            # Le os valores dos botoes
            self.botao, self.valores = self.jeito.Read()
          
            # Verifica se algum dos botoes que fazem acoes foram apertados 
            if self.botao == 'c':
                self.resultado = ''
                self.jeito.FindElement('telinha').Update(self.resultado)
            
            elif self.botao == '<-':
                self.resultado = self.resultado[:-1]
                self.jeito.FindElement('telinha').Update(self.resultado)
            elif len(self.resultado) == 16:
                pass

            # resultados e retoros de respostas em forma de float
            
            elif self.botao == '=':
                self.resposta = eval(self.resultado)
                self.resposta = str(round(float(self.resposta),3))
                self.jeito.FindElement('telinha').Update(self.resposta)
                self.resultado = self.resposta
                  
            # Fecha a janela quando solicitado
          
            elif self.botao == 'sair'  or self.botao == None:
                break
            else:
                self.resultado += self.botao
                self.jeito.FindElement('telinha').Update(self.resultado)
       

comecar = Calculadora()
comecar.Iniciar()