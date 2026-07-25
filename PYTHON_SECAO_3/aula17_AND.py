# Operadores logicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# Verdadeiras
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc ja viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
entrada = input('[E]ntrar [S]air:')
senha_digitada = input('senha: ')

senha_permitida = '123456'
#if True: so vai ser executada quando for verdadeira
if entrada == 'E' and senha_digitada == senha_permitida:
    print('entrar')
else :
    print('sair')    

#avalição de curto circuito
print(True and False and True)
print(bool(0))
senha_digitada = input('senha: ')

senha_permitida = '123456'
#if True: 
if entrada == 'E' and senha_digitada == senha_permitida:
    print('entrar')
else :
    print('sair')    


print(True and False and True)
print(bool(0))

print(True and True and True)
#ELE VAI RETORNAR true
print(True and False and True)
#ELE VAI PARAR NO FALSO E N PROSSEGUE COM O RESTANTE
# serve pára valor 0 tbm 