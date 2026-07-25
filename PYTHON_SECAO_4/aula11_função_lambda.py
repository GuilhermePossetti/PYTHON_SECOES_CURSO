"""
Função lambda em Python
A função lambda é uma função como qualquer outra em Python, porém são funções anônimas
que contém apenas uma linha. Ou seja, tudo deve ser contido dentro de uma única expressão
"""
Lista1 = [  
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def ordena(item):#Define uma função chamada ordena
    return item['sobrenome']#Retorna o valor da chave 'sobrenome' do dicionário.
#       ouuuu
Lista1.sort(key = lambda item: item['nome'])#ordena a lista no próprio lugar define qual valor usar para ordenar 

Lista1.sort(key = ordena)#

for item in Lista1:#
    print(item)#

################################### / / / / / / /#################################

def exibir(lista):
    for item in lista:
        print(item)
    print()

L1 = sorted(Lista1, key = lambda item: item['nome'])
L2 = sorted(Lista1, key = lambda item: item['sobre nome'])
exibir(L1)
exibir(L2)







################################### / / / / / / /#################################
lista= [1, 9, 51, 651, 51, 89]
lista.sort()#ordena lista, organiza
lista.sort(reverse=True)#pode inverter a ordem da lista
print(lista)