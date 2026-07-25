"""
class - Classes são moldes para criar novos objetos
As classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métados
Os objetos gerados pela classes podem usar seus dados internos para realizas várias ações
Por convenção, usamos PascalCase para nomes  de classes
"""
# quando estiver dados dentro da classe atributos, quando for chamar sem os ( parentes )
# quando tiver falando de ações dentro da classe métados

class Pessoa:
    ...

p1 = Pessoa()
p1.nome = 'luiz'
p1.sobrenome = 'carlos'

p2 = Pessoa()
p2.nome = 'lu'
p2.sobrenome = 'is'

print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)