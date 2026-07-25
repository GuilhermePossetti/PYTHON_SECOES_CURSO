"""
exiba os indeces a lista
"""

lista = ['maria', 'helena', 'Luiz']
lista.append('joao')
indices = range(len(lista))


for indice in indices:
    print(indice, lista[indice])