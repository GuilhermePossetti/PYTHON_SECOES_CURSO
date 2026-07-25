"""
Fatiamento de strings
012345678
ola mundo
-987654321
fatiamento [i: f: p:] [::]
obs.: a função len retorna a qtd
de caracteres da str
"""
variavel = 'ola mundo'
print(len(variavel[4:8]))
print(variavel[0:8:3])
# indice 4 so vai aparecer a letra m
# : serve para fazer o fatiamento
# função len serve pare contar qnts caratcteres
# e ela so funciona com strings