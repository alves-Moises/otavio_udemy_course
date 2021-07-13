from datetime import date, datetime
from random import randint

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade):   
        self.nome = nome 
        self.idade = idade
    
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)
    
    @classmethod    #cls é tipo self
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento

    @staticmethod   #tipo funções normais
    def gera_id():
        rand = randint(10000, 19999)
        return rand

p1 = Pessoa.por_ano_nascimento('Luis', 1987)
p1 = Pessoa('Luis', 32)
print(p1)
print(p1.nome, p1.idade)
print('asd', Pessoa.gera_id())
print(p1.gera_id())
