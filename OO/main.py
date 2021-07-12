from pessoa import Pessoa

p1 = Pessoa('ALves', 42)
p2 = Pessoa('joão', 32)

p1.nome = 'alves'
p2.nome = 'segunda pessoa'


print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())



print(p2.nome)
