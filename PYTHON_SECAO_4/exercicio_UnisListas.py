# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]






#                    "FORMA MANUAL DE FAZER"                       
def zipper(lista1, lista2): #Cria uma função chamada zipper que recebe duas listas. 
    intervalo_maximo = min(len(lista1), len(lista2))#min() significa menor valor // #len() significa length (tamanho) // Ele retorna quantos elementos existem na lista.
    return[(lista1[i], lista2[i]) for i in range(intervalo_maximo)] #

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte'] #
l2 =  ['BA', 'SP', 'MG', 'RJ'] #
print(zipper(l1, l2)) #



#    OU PODE USAR A FUNÇÃO ZIP PARA FAZER todo ESSE CÓDIGO



#    FUNÇÃO ZIP
from itertools import zip_longest #serve para importar uma função chamada zip_longest do módulo itertools da biblioteca padrão do Python.

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte'] 
l2 =  ['BA', 'SP', 'MG', 'RJ'] 
print(list(zip(l1, l2)))#junta os pares da L1 e L2 e para quando fizer par
print(list(zip_longest(l1, l2, fillvalue= 'Sem cidade'))) 
#Essa função pega elementos das duas listas na mesma posição e cria pares (tuplas).
#Mas diferente do zip(), ela continua até a maior lista terminar.
#Se faltar um elemento em alguma lista, ela usa o valor definido em fillvalue


#                  OBSERVAÇÕES E ANOTAÇÕES

#O for i in range() em Python serve para repetir algo várias vezes. Ele cria um laço de repetição (loop)
#(lista1[i], lista2[i]) serve para juntar em uma tupla, ele mostra as posições
# indice        lista   
#   0     →     Salvador
#   1     →     Ubatuba
#   2     →     Belo Horizonte

#   0     →     BA
#   1     →     SP
#   2     →     MG
#   3     →     RJ
# Ele vai pegar os elementos da mesma posição em duas listas e junta em um par (tupla).
#
#itertools é um módulo do Python que contém várias ferramentas para trabalhar com iterações, listas e loops
# Algumas funções desse módulo:
#                               count()
#                               cycle()
#                               zip_longest()
#                               combinations()
#zip() : Para quando uma das listas menor acabar.
#zip_longest() : continua até a lista maior acabar
#
#
#
#
#
#
#