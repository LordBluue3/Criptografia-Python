import PySimpleGUI as sg
from message import Code
import pyperclip as pc

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Texto para codificar')],
    [sg.Multiline(size=(70, 10), key='codigo'), sg.Button('Codificar')],
    [sg.Text('Texto para decodificar')],
    [sg.Multiline(size=(70, 10), key='decodificar'), sg.Button('Decodificar'), sg.Button('Copiar')]
]

# Window
window = sg.Window('Tela de criptografia', layout)

# Reading events
global message_descrypt
global message_encrypt
while True:
    events, value = window.read()
    if events == sg.WINDOW_CLOSED:
        break

    if events == 'Codificar':
        message = Code(value['codigo'], value['decodificar'])
        message_encrypt = message.encrypt()
        window.Element('decodificar').update(value=message_encrypt)
        window.Element('codigo').update(value='')
        print("Mensagem criptografada", message_encrypt)

    if events == 'Decodificar':
        cryptography = Code(value['codigo'], value['decodificar'])
        message_descrypt = cryptography.decrypt()
        window.Element('codigo').update(value=message_descrypt)
        window.Element('decodificar').update(value='')
        print(message_descrypt)

    if events == 'Copiar':
        pc.copy(message_encrypt)
