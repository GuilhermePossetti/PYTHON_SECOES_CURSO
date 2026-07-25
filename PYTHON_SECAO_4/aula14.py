"""
List comprehension em Python
List comprehension é uma forma rápida para criar listas a partir de iteráveis
"""
print(list(range(10))) #cria uma sequência de números de 0 até 9
lista = []#Cria uma lista vazia Essa lista vai ser preenchida aos poucos no for
for numero in range(10):#Inicia um laço de repetição ange(10) gera números de 0 a 9
    lista.append(numero)#append() adiciona um valor no final da lista
    print(lista)#Mostra a lista a cada iteração

lista = [numero * 2 for numero in range(10)]#Isso é uma List Comprehension (forma curta e elegante de criar listas).
#Mais curta, Mais legível, Muito usada em Pytho
print(lista)#