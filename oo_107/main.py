from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('JJ')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

# print(escritor.nome)
# print(caneta.marca)
# maquina.escrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()