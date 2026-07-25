"""
Métados de classe  +  factores (fábricas) 
São métados onde "self" será "cls", ou seja, ao invés de receber a instância
no primeiro parâmetro, receberemos a própria classe
"""

class Pessoa:
    ano = 2023 # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome    
        self.idade = idade

    @classmethod
    def metado_de_classe(cls):
        print('OLa')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Guilhermer')
print(p2.nome, p2.idade)
print(Pessoa.ano)
Pessoa.metado_de_classe()