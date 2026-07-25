# Try, except, else e finally

try:
    a = 10
    b = 0
    print('Linha 1')
    c = a / b #ERRO
    print('Linha 2')
except ZeroDivisionError: #Acontece quando você tenta dividir um número por zero.
    print('Dividiu por zero') #PULA PRA CÁ

except NameError: #Acontece quando você usa uma variável, função ou nome que não existe (não foi definido).
    print('Nome B não está defenido')

except (TypeError, IndexError): #Acontece quando você usa um tipo de dado errado em uma operação.
    #Acontece quando você tenta acessar uma posição que não existe numa lista, tupla ou string.
    print('Typer erro + IndexError')

except Exception: #é a classe base da maioria dos erros em Python
    print('erro desconhecido')

print('Continuar')

# Try e except serve para "esconder o erro" quando aparece o erro ele pula direto para oq vem dps do except
# não é uma boa pratica fazer o try assim

# try → onde você coloca o código que pode dar erro
# except → onde você diz o que fazer se der erro
# Sem try, não existe except.

# e você SABE qual erro pode acontecer → use o erro específico
# Se você NÃO sabe qual erro pode acontecer → use Exception