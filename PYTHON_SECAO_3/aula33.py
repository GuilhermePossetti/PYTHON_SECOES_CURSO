frase = 'O python é uma linguagem de programação'\
    'multiparadigma'\
    'Python foi criado por Guido van Rossum.'
#contra barra invertido é para a quebra de linha
# a palavra multiparaigma esta junto com a primeira frasa

##  como saber o tanto qual a letra que apareceu mais vezes na frase ##

# print(frase.count('python'))

i = 0
qntd_apareceu_mais_vezes = 0
letra_q_apareceu_mais_vezes = ''

while i < len(frase): 
    letra_atual = frase[i]
    qnts_vezes_apareceu_letra_atual = frase.count(letra_atual)

    if qntd_apareceu_mais_vezes < qnts_vezes_apareceu_letra_atual:          
       qntd_apareceu_mais_vezes = qnts_vezes_apareceu_letra_atual 
       letra_q_apareceu_mais_vezes = letra_atual

    i += 1

    print(
        'a letra mais vezes foi: ' 
        f'{letra_q_apareceu_mais_vezes} que apareceu'
        f'{qntd_apareceu_mais_vezes}X'
        )
  
########################################################

texto = 'python'

i = 0
tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i], i)

    i += 1

###############################

senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x):')

    repeticoes += 1

print(repeticoes)
print('aquele laço acima pode ter repetiçoes infinita')

#########################################################