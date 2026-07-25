
"""
crie uma função que multiplica todos os argumentos
não nomeados recebidos
retorne o total para uma váriavel e mostre o valor da variavel
"""

def num_multiplica(*args): #args pq pode receber qnts argumentos quiser
    total = 1
    for numero in args:
        total *= numero
    return total
    
valor_variavel = num_multiplica(2, 2, 2, 15)
print(valor_variavel)

#########################################
"""
cria uma função  fala se um número é par ou ímpar
retorne se número é par ou ímpar
"""

def par_impar(numero):
    multiplo = numero %2 == 0
    
    if multiplo:
        return f'{numero} é par'
    else:
        return f'{numero} é ímpar' 
    
print(par_impar(5))   
print(par_impar(158))   
print(par_impar(519651))   
print(par_impar(88))   

##########################################
"""
Crie uma função chamada dobro que recebe um número e retorna o dobro desse número.
Depois, teste a função com alguns números diferentes e mostre o resultado.
"""

def dobro(*numeros):
    return [numero * 2 for numero in numeros]

print(dobro(2))
print(dobro(8, 41))
print(dobro(5, 5, 80))

#########################################
"""
Exercício: verificar se um número é positivo, negativo ou zero
"""
def verifica_numero(numero):
    if numero > 0:
        return 'Positivo'
    elif numero < 0:
        return 'Negativo'
    else:
        return 'Zero'
    
print(verifica_numero(-8))
print(verifica_numero(0))
print(verifica_numero(9))

##################################
"""
Crie uma função chamada soma_lista que receba vários números e retorne a soma total deles.
"""

def soma_lista(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(soma_lista(5))
print(soma_lista(2, 3, 8))
print(soma_lista(80, 20, 30))

