from modulos.chatbot import ChatBot
from modulos.simplify import *
from time import sleep
from os import system

data = 'data/data.json'

chat_bot = ChatBot()
chat_bot.training()
training_converse = list()
old_data = list()

while True:
    chat_bot.get_response()

    if chat_bot.ask == 'exit':
        break
    elif chat_bot.ask not in chat_bot.training_data:
        if chat_bot.match > 90:
            continue
        else:
            old_data = ler_Json(old_data, data)
            new_converse = input(f'Como eu poderia responder a "{chat_bot.ask}"?: ').lower()
            old_data.append(chat_bot.ask)
            old_data.append(new_converse)
            gravar_Json(old_data, data)
    elif chat_bot.ask == 'clear':
        print('Kyon: Pera ai já vou limpar')
        sleep(1)
        print('Kyon: calma, tá uma bagunça aqui no terminal')
        sleep(2)
        system('clear')
