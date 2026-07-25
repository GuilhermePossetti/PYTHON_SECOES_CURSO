a = 'aaaa'
b = 'b'
c = 1.1
string = 'a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
    )

print(formato)

#numero detro da chaves são indice que indica
# a ordem por onde vai começar
#tudo que tiver em um parametro renomeado
#tem que renomear todos 

