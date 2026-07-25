"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)

lembre - te de desempacotamento
"""
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(x, y):
    return x + y

print(1)



#     *args Empacota vários valores em uma tupla
#     * Desempacota uma lista/tupla em vários valores
##############ACOMULAÇÕES#####################

def soma(*args): #args é uma tupla, pode passar quantos argumentos NÂO nomeados que quiser
    total = 0
    for numero in args:
        total += numero
    return total   
    

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
print(soma_4_5_6)

outra_soma = soma(1,2,3,4,5,8,7,9,6,7,8)
print(outra_soma)