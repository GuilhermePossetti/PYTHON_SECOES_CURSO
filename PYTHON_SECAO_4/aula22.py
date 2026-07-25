# Generador expression, Iterables e Iterators em PY

                       #iterable = ['Eu', 'Tenho', '___iter___']
                       #iterador = iter(iterable) #tem ___iter___ e ___next___

#Iterables tem a responsabilidade de ter outros valores
#Iterators entregar um valor por vez

#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|

# Gererator são funções que sabem pausar em determinado ocasião
# Iteretor trabalha com iterável

iterable = ['Eu', 'Tenho', '___iter___']
iterador = iter(iterable)
lista = [n for n in range(1000)]
generator = (n for n in range(1000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)