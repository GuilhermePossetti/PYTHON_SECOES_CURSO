""" Herança simples - Relações entre classes
Associação - usa outro, Agregação - tem outro
Composição - É dono de outro, Herança - É objeto

Herança ou Composição

Classe principal (Pessoa)
-> super class, base class, parent class
Classes filhas (cliente)
-> sub class, child class, derived class"""
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa): #herança
    ...

class Aluno(Pessoa): #herança
    ...

c1 = Cliente('Gui', 'Po7')
c1.falar_nome_classe()
a1 = Aluno('Gu', 'Fon')
a1.falar_nome_classe