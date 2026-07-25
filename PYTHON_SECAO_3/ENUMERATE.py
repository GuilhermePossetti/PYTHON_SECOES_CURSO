"""
enumerate - enumera iteraveis (indices)
[(0, 'maria'), (1, 'helena'), (2, 'luiz'), (3, 'joao')]
"""
lista = ['maria', 'helena', 'luiz']
lista.append('joao')

lista_unumerada = list(enumerate(lista))
print(lista_unumerada) 

# for item in lista_unumerada:
#     print(item)