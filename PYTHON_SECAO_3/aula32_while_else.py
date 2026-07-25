"""  while/else """
string = 'Valor qualquer'

i = 0 
while i < len(string):
    letra = string[i]

    print(letra)
    i += 1
else:
    print('o else foi executado')
#quando o WHILE for executado completamente 
#sem erro o else vai ser executado
#quando tiver um BREAK dentro do while o 
#else não será executado