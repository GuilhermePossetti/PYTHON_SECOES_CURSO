"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
    num_inteiro = int(input('Dig um num inteiro: '))
    if num_inteiro % 2 == 0:
        print('num dig é par')
    else:
        print('num dig é impar')
except:
    print('num n é inteiro')
#try serviu para eu executar oq esta dentro dele, se caso ouvesse um
#erro na linha 7 ele pulava para a linha 12


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
try:
    hora = int(input('Digite a hora em num inteiro: '))
    if hora >= 0 and hora <= 11:
        print('bom dia')
    elif hora >= 12 and hora <= 17:
        print('boa tarde')
    elif hora >= 18 and hora <= 23:
        print('boa noite')
    else:
        print('essa hora n existe')
except:
    print('Difite num inteiro')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('nome curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('normal')
    elif tamanho_nome >= 7:
        print('longo')
    else:
        print('nome longo')
else:
    print('Digite mais letra')

