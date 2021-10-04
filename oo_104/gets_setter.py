# seeter = configurando um valor (=)

# getter = obter um valor (.)

class Pessoa:
    def __init__(self, nome) -> None:
        print('initi')
        self.nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        print('Setter executado')
        nome += 'seila'
        self._nome = nome

    @property
    def sobrenome(self):
        return 'Desconhecido'

p1 = Pessoa('Nome')
# p1.nome = 'joão'
print(p1.nome)
print(p1.sobrenome)
