"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def encontra_primeiro_duplicado(lista_de_inteiros):#Cria uma função chamada encontra_primeiro_duplicada Ela recebe uma lista de números como parâmetro
    numeros_checados = set()#Cria um set (conjunto) vazio. Não aceita valores repetidos Busca valores muito rápido Será usado para guardar números já vistos.
    primeiro_duplicado = -1#Inicializa a variável com -1 não encontrei número duplicado

    for numero in lista_de_inteiros:#Percorre cada número da lista recebida. A cada volta numero recebe um valor da lista
        if numero in numeros_checados:#Verifica se o número já foi visto antes Se estiver no set, então ele é duplicado
            primeiro_duplicado = numero#Guarda o número duplicado encontrado. 
            break#Interrompe o loop imediatamente.

        numeros_checados.add(numero)#Adiciona o número ao conjunto numeros_checados

    return primeiro_duplicado#O número duplicado encontrado
                             #Ou -1 se não houver duplicados

for lista in lista_de_listas_de_inteiros:#Percorre cada lista interna da lista principal. a cada volta lista recebe uma das listas
    print(lista,encontra_primeiro_duplicado(lista))#Mostra a lista atualChama a função Mostra o primeiro número duplicado dessa lista


########################################################################################################################################################################

listas = [
    [1, 2, 3, 2],
    [5, 6, 7, 8],
    [9, 1, 9, 3],
]

def encontra_primeiro_repetido(lista):
    vistos = set()

    for numero in lista:
        if numero in vistos:
            return numero
        vistos.add(numero)

    return -1

for l in listas:
    print(l, "→", encontra_primeiro_repetido(l))