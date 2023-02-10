from datetime import date
import json
import colorama
from os import system, name

def obter_data():
    data_atual = date.today()
    format_date = f'{data_atual.day}/{data_atual.month}/{data_atual.year}'
    return format_date

def ler_Json(objeto, arquivo):
    file_load = arquivo
    with open(file_load) as file:
        objeto = json.load(file)
    return objeto

def gravar_Json(objeto, arquivo):
    with open(arquivo, 'w') as file:
        json.dump(objeto, file, indent=2)

def colorir(texto, cor):
    colorama.init()

    if cor == 'vermelho':
        texto_colorido = colorama.Fore.RED + texto
    elif cor == 'verde':
        texto_colorido = colorama.Fore.GREEN + texto
    elif cor == 'azul':
        texto_colorido = colorama.Fore.BLUE + texto
    elif cor == 'amarelo':
        texto_colorido = colorama.Fore.YELLOW + texto
    elif cor == 'magenta':
        texto_colorido = colorama.Fore.MAGENTA + texto
    elif cor == 'ciano':
        texto_colorido = colorama.Fore.CYAN + texto
    elif cor == 'branco':
        texto_colorido = colorama.Fore.WHITE + texto
    elif cor == 'cinza':
        texto_colorido = colorama.Fore.LIGHTBLACK_EX + texto
    elif cor == 'vermelho claro':
        texto_colorido = colorama.Fore.LIGHTRED_EX + texto
    elif cor == 'verde claro':
        texto_colorido = colorama.Fore.LIGHTGREEN_EX + texto
    elif cor == 'azul claro':
        texto_colorido = colorama.Fore.LIGHTBLUE_EX + texto
    elif cor == 'amarelo claro':
        texto_colorido = colorama.Fore.LIGHTYELLOW_EX + texto
    elif cor == 'magenta claro':
        texto_colorido = colorama.Fore.LIGHTMAGENTA_EX + texto
    elif cor == 'ciano claro':
        texto_colorido = colorama.Fore.LIGHTCYAN_EX + texto
    else:
        texto_colorido = colorama.Fore.BLACK + texto
    return texto_colorido

def banner(msg):
    print('-=' * 20)
    print(f'{msg.upper():^40}')
    print('-=' * 20)
    print('\n')

def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')