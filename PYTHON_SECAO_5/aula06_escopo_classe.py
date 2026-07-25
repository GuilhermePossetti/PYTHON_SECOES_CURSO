class Animal:

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
    
    def execultar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)
    
leao = Animal(nome= 'Leão')
print(leao.nome)
print(leao.execultar('maçã'))

#                    **  OBSERVAÇÃO  **

# * uma váriavel definida dentro de um método não pode ser chamado dentro de outro métado *
# * a não ser que seja usando o self *