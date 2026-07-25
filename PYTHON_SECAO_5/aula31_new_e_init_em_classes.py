"""__new__ e __init__ em classes Python
__new__ é o método responsável por criar e retornar o novo objeto
Por isso, new recebe cls
__new__ ! DEVE retornar o novo objeto !
__init__ é o método responsavel por iicializar
a instância. Por isso, init recebe self.
__init__ ! NÂO DEVE retornar nada (None) !
object é a super classe de uma classe
"""

class A:

    def __new__(cls, *args, **kwargs):
        isinstancia = super().__new__(cls)
        return isinstancia
    
    def __init__(self, x):
        self.x = x
        print('SOuo init')

    def __repr__(self):
        return 'A()'

a= A()