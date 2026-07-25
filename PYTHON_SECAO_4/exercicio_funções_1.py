"""
Crie funcões que duplicam, triplicam e quadriplicam
o numero recebido como parametro
"""

def duplicar(numero):
    return numero * 2

def triplicar(numero):
    return numero * 3

def quadriplicar(numero):
    return numero * 4
    
print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))

#################### OU ######################

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicarr = criar_multiplicador(2)
triplicarr = criar_multiplicador(3)
quadruplicarr = criar_multiplicador(4)

print(duplicarr(2))
print(triplicarr(2))
print(quadruplicarr(2))

