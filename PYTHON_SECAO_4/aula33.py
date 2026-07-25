# Variáveis livres + nonlocal

# Variáveis livres + nonlocal (locals, globals)
# print(globals())
# def fora(x):
#     a = x

#     def dentro():
#         # print(locals())

#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())
def concatenar(string_inicial): #função que recebe um valor inicial
    valor_final = string_inicial #recebe também o valor de string_inicial

    def interna(valor_a_concatenar=''):#Ela recebe o valor que você passa quando chama c()
        nonlocal valor_final#usar a variável valor_final da função externa permite modificar valor_final da função externa
        valor_final += valor_a_concatenar#Então ele acumula os valores anteriores.
        return valor_final#ele retorna toda a string acumulada.
    return interna#Essa função retorna a função interna.


c = concatenar('5')#Ela recebe a função interna.
print(c('2'))#
print(c('3'))#
print(c('4'))#
final = c()#ela faz final ser o resultado da função
print(final)#