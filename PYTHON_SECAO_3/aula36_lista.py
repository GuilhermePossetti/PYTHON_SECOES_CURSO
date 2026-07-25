"""
listas em python
tipo list - mutavel
suporta varios valores de qualquer tipo
conhecimentos reutilizaveis - indice e fatiamento
metodos uteis:  appen, insert, pop, del, clear, extend, +
creat read update  delete
criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#         01234
#        -54321
string = 'ABCDE' #5 caracter (len)
lista = [] #ou
lista = list()
#duas formas de usar o comando list [] ou list()
#lista fazia == falsa

#        0     1        2       3
#       -4    -3       -2      -1       
# alterar 
lista= [123, True, 'guilerme', 1.2]
lista[-2] = 'maria' #alterei o nome guilherme para maria
print(lista) #indice -2 e 2 nesse caso é a mesma coisa escrita
print(lista[2])

#apagar lista
lista = [10, 20, 30, 40]
lista[2] = 300 #alterei o indice 2 == 30 para 300
del lista[2] #apaguei o indice 2 == 300 para nada pq apaguei
print(lista)
print(lista[2]) #isso e só para aparecer o valor do indice 2

#adicionar mais coisas na lista
lista = [10, 20, 30, 40]
lista.append(50) #adiciona ao final da lista
lista.pop() #remove o ultimo numero da lista
print(lista)

"""
append - adiciona um item ao final
insert - adiciona um item no indice escolhido
pop - remove do final ou do indice escolhido
del - apaga um indice
clear - limpa a lista
extend - estende a lista
+ - concatena lista
creat read update delete
criar ler  alterar apagar = lista[i] (CRUD)
"""
#         0   1   2   3
lista = [10, 20, 30, 40]
lista.insert(0, 5) #insert serve para adicional um valor na lista
#(0, 5) o primeiro numero e referente ao indice escolhido, em qual
#lugar eu vou mudar//////// o segundo valor serve para qual valor eu vou colocar
#mais pode ser alguma string (0, 'gui' )
print(lista)

############---concatenação---############

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b) #esse métado n retorna nada ele vai estender
print(lista_d)
