from modulos.simplify import *
from time import sleep
from random import randint, choice

palpites_maior = ['Que porra de chute é esse? calma ai neymar, menos que isso...', 'Passou longe, é menos que isso...', 'calma vida tá nervoso? menos...', 'kkkkk você é foda hein, eu disse menor...', 'tô me cansando disso kkkkkk']
palpites_menor = ['Um pouco maior...', 'Quase lá, é um pouco maior, tenta de novo...', 'Tô me cansando disso kkkkk...', 'Soma o tamanho do seu pau mais 2cm, é por ai!']

class ChatBot():
    def __init__(self):
        self.training_data = list()
    
    def training(self):
        self.training_data = ler_Json(self.training_data, 'data/data.json')
    
    def get_response(self):
        self.ask = input('Você: ')

        if self.ask in self.training_data:
            index = self.training_data.index(self.ask) + 1
            print(f'Kyon: {self.training_data[index]}')

        if self.ask not in self.training_data:
            print('Kyon: Eu não tenho uma resposta pra isso.')
    
    def game_adivinhar(self):
        number = randint(1, 50)
        print('Kyon: Eu pensei em um número de 1 a 50, tente adivinhar...')
        while True:
            ask = int(input('Você: '))
            if ask < number:
                print(f'Kyon: {choice(palpites_menor)}')
            elif ask > number:
                print(f'Kyon: {choice(palpites_maior)}')
            elif ask == number:
                print(f'Kyon: finalmente acertou')
                break
        
