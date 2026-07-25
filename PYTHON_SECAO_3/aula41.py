"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = 'olha so que, coisa interessante'
lista_frases = frase.split(',')

for i, frase in enumerate(lista_frases):
   
   
    print(lista_frases[i].strip)#strip corta os espaços do começo e do final da string
                                #rstrip corta o espaço da direita
                                #lstrip corta o espaço da esquerda
print(lista_frases)

########## join ##############

frases_unidas = ' '.join( lista_frases)
print(frases_unidas)
# as aspas vazias dps do frase_unidas serve para eu colocar alguma coisa
#join( colocar alguma string ) join so funciona com iteraveis