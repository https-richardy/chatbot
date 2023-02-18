from modulos.simplify import *
from time import sleep
from fuzzywuzzy import fuzz
from os import system
from gtts import gTTS
from playsound import playsound

class ChatBot():
    def __init__(self):
        self.training_data = list()
    
    def training(self):
        self.training_data = ler_Json(self.training_data, 'data/data.json')
    
    def get_response(self):
        self.ask = input('Você: ').lower()
        for speech in self.training_data:
            self.match = fuzz.token_set_ratio(self.ask, speech)
            index = self.training_data.index(speech) + 1
            if self.match > 60:
                audio = gTTS(self.training_data[index], lang='pt')
                audio.save('kyon_speech.mp3')
                playsound('kyon_speech.mp3')
                print(f'kyon: {self.training_data[index]}')
                break
            else:
                continue

        if self.ask not in self.training_data:
            if self.match > 60:
                pass
            else:
                print('Kyon: Eu não tenho uma resposta pra isso.')

    def get_date(self):
        self.data = obter_data()