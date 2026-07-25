"""
INTRODUÇÃO AO DESEMPACOTAMENTO + TUPLES (TUPLAS)
"""

nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes
print(nome1)
print(nome2)
print(nome3)
######################################
nome1, *_ = ['Maria', 'Helena', 'Luiz']
print(nome1)
#para empacotamento só uma variavel fazer assim
#sempre que for pegar um valor e sobrar tem q fazer 
#isso para o resto que sobra ou usar o anderline _