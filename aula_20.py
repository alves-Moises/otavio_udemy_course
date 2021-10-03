nome = 'alves'

idade = 23
altura = 1.5
peso = 66.0
ano_atual = 2021
ano = ano_atual - idade
imc = (peso/(altura ** 2))

print(f'''
    nome: {nome}
    idade: {idade}
    altura: {altura}
    peso: {peso}
    ano atual: {ano_atual} 
    ano de nascimento: {ano}
    imc: {imc:.2f}
''')