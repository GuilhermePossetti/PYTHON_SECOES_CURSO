texto = 'python'

novo_texto = '' 
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto)

################################

"""  
for + range   
range -> range(start, stop, step)


start → valor inicial da sequência (inclusivo).
stop → valor final (exclusivo, ou seja, o stop não entra).
step → incremento (de quanto em quanto a sequência vai andar).
"""
#                ^     ^       ^
numeros = range( 0,    20,     2)
for numero in numeros:
    print(numero)

##############################################################

"""
iterável -> str, range, etc...
iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador
"""
numeros = range(0, 20, 2)
for numero in numeros:
    print(numero)

##########################
texto = iter('luiz')
print(iter(texto))

print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))

for letra in texto:
    print(letra)

