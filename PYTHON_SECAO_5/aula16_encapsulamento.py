"""
 Encapsulamento (modificadores de acesso: public, protectd, private)
 Python NÃO TEM modificadores de acesso
 Mas podemos seguir as seguintes convenções
 ( )(sem underline) = public, pode ser usado em qualquer lugar
 (_) (um underline) = protectd, não deve ser usado fora da classe ou subclasses, só dentro das classes
 (__) (dois underline) = private, "name mangling" (desfiguração de nomes) em Python
 só deve ser usado na classe em que foi declarado
"""
### ( )(sem underline) = public, pode ser usado em qualquer lugar
class Foo:
    def __init__(self):
        self.public = 'Isso é público'

    def metodo_publico(self):
        return 'medoto_publico'

f = Foo()
print(f.public)        
print(f.metodo_publico())


#################################################################################
print()
print()
#################################################################################


## (_) (um underline) = protectd, não deve ser usado fora da classe ou subclasses
class Foo:
    def __init__(self):
        self.public = 'Isso é público'
        self._protected = 'Isso é protegido'

    def metodo_publico(self):
        return 'medoto_publico'
    
    def _metodo_protected(self):
        return '_metoo_protected'

f = Foo()
print(f._protected)
print(f._metodo_protected())


#################################################################################
print()
print()
#################################################################################


## (__) (dois underline) = private, "name mangling" (desfiguração de nomes) em Python
class Foo:
    def __init__(self):
        self.public = 'Isso é público'
        self._protected = 'Isso é protegido'
        self.__private = 'Isso é privado'

    def metodo_publico(self):
        return 'medoto_publico'
    
    def _metodo_protected(self):
        return '_metoo_protected'

    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'

f = Foo()

