""" 
REPETIÇÕES
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""
condicao = True

while condicao:
    nome = input('Qual seu nome: ')
    print(f'Seu nome é: {nome}')

    if nome == 'Sair':
        break #brak para o laço de repetição

print('Acabou')
####################
contador = 0

while contador < 10:
    contador = contador + 1
    print(contador)

print('acabou')
##################### a palavra continue é ignora o resto do código 
# daquela volta do loop mas o loop continua rodando

###EXEMPLO###

# for numero in range(1, 6):
#     if numero == 3:
#         continue  # pula o número 3
#     print(numero)

contador = 0 

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break

print('acabou')

