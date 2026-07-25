def soma(a, b):
    return a + b
resultado = soma(4 , 6)
print(resultado)


#############################################################

def dobro(numero):  
    return numero * 5
resultadoo = dobro(1)
print(resultadoo)

##############################################################

def eh_positivo(numero):
    if numero >= 0:
        return True
    else:
        return False
reesultado = eh_positivo(-15)
print(reesultado)

###############################################################

def maior_numero(a, b):
    if a > b:
        return a
    else:
        return b
rresultado = maior_numero(5, 9)
print(rresultado)

################################################################

def eh_par(numero):
    if numero %2 == 0:
        return True
    else:
        return False
rreesultado = eh_par(15)
print(rreesultado)

##################################################################

def contar_letras(str):
    return len(str)
rreesultadu = contar_letras('Gui')
print(rreesultadu)


###################################################################

def palavra_grande(texto):
    if len(texto) >= 5:
        return 'Grande'
    else:
        return 'Pequeno'
rezultadu = palavra_grande('Gui')
print(rezultadu)

###################################################################

def pode_dirigir(numero):
    if numero >= 18:
        return 'Pode dirigir'
    else:
        return 'Não pode dirigir'
ressultadu = pode_dirigir(1)
print(ressultadu)

####################################################################

def verificar_senha(texto):
    if len(texto) >= 8:
        return 'Senha válida'
    else:
        return 'Senha muito curta'
res = verificar_senha('gui')
print(res)

######################################################################

def maior_de_idade(numero):
    if numero >= 18:
        return 'Maior de idade'
    else:
        return 'Menor de idade'
resulrado = maior_de_idade(19)
print(resulrado)

######################################################################

while True:
    try:
        numero_digitado=int(input('digite um numero '))
        if numero_digitado == 0:
            print('Programa encerrado')
            break
        print(numero_digitado)

    except:
        print('digite apenas numeros')

######################################################################

