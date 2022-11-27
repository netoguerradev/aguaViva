import PySimpleGUI as sg
from index import *


def window_1():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Controle de gestão de recursos hídricos do hotel',pad=(10,10))],
        [sg.Text('Digite o numero do quarto[1/36]',size=(25,1),pad=(10,10)),sg.InputText()],
        [sg.Button('Entrar no quarto',pad=(10,10))],
        [sg.Text('aguaViva©',pad=(20,20))]
    ]
    return sg.Window('Dashboard',layout=layout,finalize=True,element_justification='c')


def window_2():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Informações do quarto',pad=(10,10))],
        [sg.Text(""+inoConnect())],
        [sg.Button('Voltar',pad=(10,10)),sg.Button('Atualizar')],
        [sg.Text('aguaViva©',pad=(20,20))]
    ]
    return sg.Window('Quarto 1',layout=layout,finalize=True,element_justification='c')


win1,win2 = window_1(),None

while True:
    window,event,values = sg.read_all_windows()

    if window == win1 and event == sg.WIN_CLOSED:
        break
    if window == win1 and event == 'Entrar no quarto' and values[0] == '1':
        win2 = window_2()
        win1.hide()
    if window == win2 and event == 'Voltar':
        win2.hide()
        win1.un_hide()
    if window == win2 and event == 'Atualizar':
        win2.refresh()
    if window == win1 and event == 'Entrar no quarto' and values[0] != '1':
        sg.popup('Este quarto não existe, ou não está conectado.')

