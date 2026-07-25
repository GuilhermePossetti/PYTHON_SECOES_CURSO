# def contador_regressivo(numero):
#     while numero >= 0:
#         print(numero)
#         numero -= 1
# contador_regressivo(10)
   




# def maior_numero(lista_de_numeros):
#     maior_numero = max(lista_de_numeros)
#     return maior_numero
# lista = [51, 8198, 651, 65181, 6511, 981891]
# maior_numero_da_lista = maior_numero(lista)
# print(f'O maior numero da lista é {maior_numero_da_lista}')





# def dobro(numero):
#     numero_dobrado = numero *2
#     return numero_dobrado
# resultado = dobro(5611)
# print(f'O numero dobrado é {resultado}')


# def par_ou_impar(numero):
#     if numero %2 == 0:
#       return 'Esse numero é par'
#     else:
#       return 'Esse numero é impar'

# resultado = par_ou_impar(6)
# print(resultado)


# def maior_numero(n1, n2):
#     if n1 > n2:
#         return f'o maior numero é {n1}'
#     elif n2 > n1:
#         return f'o maior numero é {n2}'
#     else:
#         return 'Os numeros são iguais'
    
# print(maior_numero(2, 22))

# #com mais parametro agora

# def mais_parametro_numero_maior(*numero):
#     maior = max(numero)
#     if numero.count(maior) > 1:
#         return 'Esse numero é repetido'
#     else:
#       return f'o maior numero é: {maior}'
# numeros = (52, 52, 53)
# resultado = mais_parametro_numero_maior(*numeros)
# print(resultado)



# def media_numeros(n1, n2):
#     media = (n1 + n2) /2
#     return media
# media_final = media_numeros (10, 50)
# print(media_final)


# def numero_dobrado(*numero):
#     return [n * 2 for n in numero]
# print(numero_dobrado(5, 5))

# def numero_quadrado(numero):
#     quadrado = numero
#     return quadrado **2 
# resultado = numero_quadrado
# print(resultado(10))




# def analisar_notas(notas):
#     if len(notas) == 0:
#         return "Lista vazia"
#     soma = 0
#     maior = notas[0]
#     menor = notas[0]
#     for nota in notas:
#         soma += nota
#         if nota > maior:
#             maior = nota
#         if nota < menor:
#             menor = nota
#     media = soma / len(notas)
#     if media >= 7:
#         situacao = "Aprovada"
#     else:
#         situacao = "Reprovada"
#     return media, maior, menor, situacao
# notas_alunos = [5.9, 9.9, 1.0, 7.8, 8.8, 8.9]
# resultado = analisar_notas(notas_alunos)
# print("Média:", resultado[0])
# print("Maior nota:", resultado[1])
# print("Menor nota:", resultado[2])
# print("Situação:", resultado[3])


# def somar_lista(valores):
#     soma = 0

#     for numeros in valores:
#         soma += numeros
#     return soma

# lista = [10, 10, 10]

# resultado = somar_lista(lista)
# print(resultado)



# def contar_maiores(numeros):
#     contador = 0
#     for numero in numeros:
#         if numero > 5:
#             contador += 1
#     return contador

# lista = [5, 6]

# resultado = contar_maiores(lista)
# print(f'quantidade de numeros maiores que cinco na lista são: {resultado}')



# def contar_negativos(numeros):
#     contador = 0
#     for numero in numeros:
#         if numero < 0:
#             contador += 1
#     return contador

# lista = [-9, -9]

# resultado = contar_negativos(lista)
# print(resultado)


# def contar_zeros(numeros):
#     contador = 0
#     for numero in numeros:
#         if numero == 0:
#             contador += 1
#     return contador

# lista = [0, 0 ,0, ]

# resultado = contar_zeros(lista)
# print(resultado)


# def contar_posi_nega(numeros):
#     positivo = 0
#     negativo = 0

#     for numero in numeros:
#         if numero > 0:
#             positivo += 1
#         elif numero < 0:
#             negativo += 1
#     return positivo, negativo

# lista = [1, 2, 3, -6, -9, -9, 0, 5]
# positivo, negativo = contar_posi_nega(lista)
# print(f'Positivos{positivo}')
# print(f'negativos {negativo}')


# def contar_pares(numeros):
#     contador = 0
#     for numero in numeros:
#         if numero %2 ==0:
#             contador += 1
#     return contador
# lista = [2, 3, 4, 5]
# resultado = contar_pares(lista)
# print(resultado)
            

# def primeiro_maior_que_cinco(numeros):
#     resultado = []
#     for numero in numeros:
#         if numero > 5:
#             resultado.append(numero)
#     if len(resultado) == 0:
#         return 'Nenh8um numero'
    
#     return resultado

# lista = [1, 2, 5, 9]
# resultado = primeiro_maior_que_cinco(lista)
# print(resultado)


# def tem_negativo(numeros):
#     for numero in numeros:
#         if numero < 0:
#             return True
#     return False
# lista = [1, -1]
# resultado = tem_negativo(lista)
# print(resultado)


# def somar_pares(numeros):
#     soma = 0
#     for numero in numeros:
#         if numero %2 == 0:
#             soma += numero 
#     return soma

# lista = [2, 2, 3, 6]
# resultado = somar_pares(lista)
# print(resultado)


# def contar_pares_maiores_que_5(numeros):
#     contador = 0
#     for numero in numeros:
#         if numero %2 == 0 and numero >= 5:
#             contador += 1
#     return contador

# lista = [2, 6, 10]
# resultado = contar_pares_maiores_que_5(lista)
# print(resultado)

# def contar_num_impares(numeros):
#     contar = 0
#     for numero in numeros:
#         if numero %2 !=0 and numero <= 5:
#             contar +=1
#     return contar
# lista = [1,3,4]
# resultado = contar_num_impares(lista)
# print(resultado)            
            

# def contar_numeros_dificil(numeros):
#     numeros_guardados = []
#     contador = 0
#     for numero in numeros:
#         if numero %2 ==0 and numero >= 10 and numero <= 50:
#             contador += 1
#             numeros_guardados.append(numero)
#     return numeros_guardados, contador
# lista = [4, 10, 20, 51]
# resultado = contar_numeros_dificil(lista)
# print(resultado)



# def filtrar_numeros(numeros):
#     lista_de_numeros = []
#     contador = 0
#     for numero in numeros:
#         if numero > 10 and numero %2 == 0:
#             lista_de_numeros.append(numero)
#             contador += 1
#     return lista_de_numeros, contador

# lista = [12,0,2,20]
# resultado = filtrar_numeros(lista)
# print(resultado)



# def analisar_nota(notas):
#     lista_notas_aprovadas = []
#     contador = 0
#     for nota in notas:
#         if nota >= 7.0:
#             lista_notas_aprovadas.append(nota)
#             contador += 1
#     if contador > 0:
#         soma = 0
#         maior = lista_notas_aprovadas[0] #esse zero é um valor base para comparar com as notas e define a maior nota
#         for nota in lista_notas_aprovadas:
#             soma += nota
#         media = soma / contador
#     else:
#         media = 0
#         maior = 0
#     return lista_notas_aprovadas, contador, media, maior
# lista = [5.0, 2.5, 5.8, 2.0, 4.8, 2.0, 8.2]
# resultado = analisar_nota(lista)

# print(f'notas do aprovado, {resultado[0]}')
# print(f'quantidade, {resultado[1]}')
# print(f'media, {resultado[2]:.2f}')
# print(f'maioor nota, {resultado[3]}')


# def contar_impares_maiores_que_10(numeros):
#     lista_todos_numeros = []
#     contador = 0

#     for numero in numeros:
#         if numero %2 != 0 and numero > 10:
#             contador += 1
#     return contador

# lista = [12,15,19,20]
# resultado = contar_impares_maiores_que_10(lista)
# print(resultado)

# def retonando_num_maiores_que_15(numeros):
#     lista_num = []
#     for numero in numeros:
#         if numero > 15:
#             lista_num.append(numero)
#     return lista_num
# lista = [18,20,30,69,51,1,2,5,14,15]
# resultado = retonando_num_maiores_que_15(lista)
# print(resultado)


# def primeiro_número_maior_que_20(numeros):
    
#     for indice, numero in enumerate(numeros):
#         if numero > 20:
#             return numero
#     return None

# lista = [2, 30,5,5,8,90,8]
# resultado = primeiro_número_maior_que_20(lista)
# print(resultado)

# def posicao_menor(numeros):
#     menor = numeros[0]
#     indice_menor = 0
    
#     for indice, numero in enumerate(numeros):
#         if numero < menor:
#             menor = numero
#             indice_menor = indice
#     return indice_menor
        
# lista = [15, 25, 30, 10]
# resultado = posicao_menor(lista)
# print(f'O numero menor está na posição: {resultado}')







# def maiores_que_dez(numeros):
#     contador = 0
#     for numero in numeros:
#         if numero > 10:
#             contador += 1
#     return contador
# lista = [10,0,3,10]
# resultado = maiores_que_dez(lista)
# print(resultado)


# def recebendo_numeros(numeros):
#     lista_pares = []
#     for numero in numeros:
#         if numero % 2 == 0:
#             lista_pares.append(numero)
#     return lista_pares
# lista = [10,0,3,1]
# resultado = recebendo_numeros(lista)
# print(resultado)    


# def recebendo_lista_impares_maiores_dez(numeros):
#     contador = 0
#     for numero in numeros:
#         if numero % 2 != 0 and numero > 10:
#             contador += 1
#     return contador
# lista = [1, 2, 3, 11]
# resultado = recebendo_lista_impares_maiores_dez(lista)
# print(resultado)


# def retornando_maior_num_lista(numeros):
#     maior = numeros[0]
#     for numero in numeros:
#         if numero > maior:
#             maior = numero
#     return maior
# lista = [1, 2, 3, 11, 5, 89, 88]
# resultado = retornando_maior_num_lista(lista)
# print(resultado)
          

# def numeros_maior_dez_maior_num_lista(numeros):
#     contador = 0
#     maior = numeros[0]

#     for numero in numeros:
#         if numero > 10:
#             contador += 1
#         if numero > maior:
#            maior = numero
#     return contador, maior
# lista = [1, 2, 3, 5, 89, 88]
# resultado = numeros_maior_dez_maior_num_lista(lista)
# print(resultado)


# def fazendo_tres_coisas(numeros):
#     contador = 0
#     maior = numeros[0]
#     lista_maior_10 = []

#     for numero in numeros:
#         if numero % 2 == 0:
#             contador += 1
#         if numero > maior:
#             maior = numero
#         if numero > 10:
#             lista_maior_10.append(numero)
#     return contador, maior, lista_maior_10

# lista = [4, 11, 20, 3, 18]
# resultado = fazendo_tres_coisas(lista)
# print(resultado)

"""
*args → quando você quer aceitar vários valores do mesmo tipo
Ex.: somar números, analisar uma lista de notas, calcular média.
*args é uma forma de dizer para a função:
“Pegue todos os argumentos posicionais que sobrarem e junte.”

**kwargs → quando você quer aceitar informações nomeadas e variáveis
Ex.: cadastro, configurações, filtros.
"""