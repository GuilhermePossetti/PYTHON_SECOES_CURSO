try:
    print('Abriu o arquivo')
    8 / 0 #erro
except ZeroDivisionError: #só entra nesse except se realmente tiver esse erro
    print('Dividiu o zero')
else:
    print('não deu erro') #se caso não ocorrer erro
finally: #sempre será executado mesmo com o erro
    print('Fechar arquivo')

