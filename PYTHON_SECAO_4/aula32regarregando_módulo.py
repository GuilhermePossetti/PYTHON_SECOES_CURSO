import imaplib #biblioteca padrão do Python usado para interagir com servidores de e-mail

import aula32m

print(aula32m.variavel)

for i in range(10):
    imaplib.reload(aula32m)
    print(i)
print('FIM')