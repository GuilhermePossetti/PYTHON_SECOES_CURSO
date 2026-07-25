"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor

Exemplo: 
Lista_A = [1, 2, 3, 4, 5, 6, 7, 8]
Lista_B = [1, 2, 3, 4, 5]

resultado = 

lista_soma = [2, 4, 6, 8, 10]
"""

listaA = [1, 2, 3, 4, 5, 1, 2, 1]
listaB = [1, 2, 3, 4, 5, 9, 5, 9 , 85, 9]

lista_soma = []

for i in range(min(len(listaA), len(listaB))):
    soma = listaA[i] + listaB[i]
    lista_soma.append(soma)

print(lista_soma)

# ou dessa forma mais simples

lista_soma = [x + y for x, y in zip(listaA, listaB)]
print(lista_soma)
    

"""
for i in range(...) serve pra quê?
Serve pra repetir um bloco de código várias vezes.
O range(...) define quantas vezes o loop vai rodar.


E o que é o i?
O i é uma variável que guarda o valor atual da repetição.
A cada volta do loop, o i muda.

min() pega o menor valor, mas depende do que você coloca dentro dele

O que o len() faz?
Ele retorna a quantidade de elementos que tem na lista.
lista = [10, 20, 30, 40]
Ex: len(lista) → 4

.append() = adicionar no final da lista
você usa isso pra ir construindo a lista resultado

"""