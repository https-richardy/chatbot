from modulos.simplify import *
from os import system
data = list()

while True:
    system('clear')
    user_option = int(input("""
[ 1 ] - Treinar com dados existente.
[ 2 ] - Novos dados.
[ 3 ] - Sair do setup de treinamento.

[ Escolha ]--> """))

    if user_option == 1:
        system('clear')
        banner('setup de treinamento')
        data = ler_Json(data, 'data/data.json')
        while True:
            pergunta = input('Digite uma fala [0 cancela]: ')
            if pergunta == '0':
                gravar_Json(data, 'data/data.json')
                break
            resposta = input(f'\nComo eu deveria responder a "{pergunta}"?: ')
            data.append(pergunta)
            data.append(resposta)
    elif user_option == 2:
        system('clear')
        banner('new data')
        while True:
            pergunta = input('Digite uma fala [0 cancela]: ').lower()
            if pergunta == '0':
                gravar_Json(data, 'data/data.json')
                break
            resposta = input(f'\nComo eu deveria responder a "{pergunta}"?: ')
            data.append(pergunta)
            data.append(resposta)
    elif user_option == 3:
        system('clear')
        break