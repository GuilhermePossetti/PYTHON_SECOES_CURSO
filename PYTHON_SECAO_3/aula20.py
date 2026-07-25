# # Operadores in e not in
# # Strings são iteráveis = vc pode navegar item por item
# # objeto que entrega os valores do iterável, um por vez.
# # 0 1 2 3 4 5 6 7 8
# # g u i l h e r m e
# #-9-8-7-6-5-4-3-2-1
# # cada letra do meu nome tem um valor G = 0 ou -9
# # U = 1 ou -8
# # in significa ESTÁ ENTRE 
# # not in NÃO ESTÁ ENTRE
nome = 'guilherme'
print(nome[2])
print(nome[5])
#AQUI ESTOU USANDO O COLCHETE PARA COLOCAR UM NUMERO
#ESSE NUMERO VAI MOSTRAR QUAL LETRA Q VAI APARECER NO TERMINAL
#STRING EM PY SÃO ITERÁVEIS
print('gui' in nome)
print('zero' in nome)
print(15 * '-')
print('gui' not in nome)
print('zero' not in nome)

print(15 * '-')

nome1 = input('Digite seu nome: ')
encontrar =input('Digite o que deseja encontrar: ')

if encontrar in nome1:
    print(f'{encontrar} esta em {nome1}')
else:
    print(f'{encontrar} não esta em {nome1}')



