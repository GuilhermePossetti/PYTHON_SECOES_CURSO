"""
introdução ao Try/except
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('Vou dobrar seu numero')

try:
    numero_float = float(numero_str)
    print('float:', numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('isso n e um numero') 

"""
o try é usado para tratar erros (exceções) que podem ocorrer 
durante a execução do programa. Ele funciona junto com except

try: bloco onde você coloca o código que pode gerar erro.
except: bloco executado se ocorrer um erro. Você pode especificar 
o tipo do erro

"""