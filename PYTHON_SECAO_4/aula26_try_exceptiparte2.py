try:
    a = 10
    b = 0
    print('Linha 1')
    c = a / b #ERRO
    print('Linha 2')
except ZeroDivisionError: 
    print('Dividiu por zero') 

except NameError: 
    print('Nome B não está defenido')

except(TypeError, IndexError) as error: #Guarde o erro que aconteceu dentro da variável error
    print('Typer erro + IndexError')    #Você não pega só a mensagem do erro. Você pega o objeto inteiro do erro.
    print('MGS:', error)
    print('NOME:', error.__class__.__name__) #Mostra o nome da classe do erro, ou seja, o tipo exato da exceção
except Exception: 
    print('erro desconhecido')

print('Continuar')

