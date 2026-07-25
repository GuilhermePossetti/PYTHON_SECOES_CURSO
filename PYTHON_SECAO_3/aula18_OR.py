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

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input(' Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
     print('Entrar')
#os parentese entre as condições serve para que o sistema resolva primeiro
# se tiver aluguma expressão com OR r AND 
#expressão ambígua uma expressão que pode gerar dúvida na interpretação, 
# seja para o programador que lê o código ou até para o próprio interpretador
else:
     print('Sair')
#and → se encontra um falso, para.
#or → se encontra um verdadeiro, para.
#Retornam o último valor avaliado, não só True/False.

# Avaliação de curto circuito
senha = input ('senha: ') or 'sem senha'
print(senha)