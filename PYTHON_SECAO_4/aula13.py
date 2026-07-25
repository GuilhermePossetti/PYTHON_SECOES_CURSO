# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
print(a, b)
pessoa = {'nome': 'Aline',
          'sobrenome': 'Souza',}
(a1, a2), (b1, b2), = pessoa.items()
print(a1, a2)
print(b1, b2)

for chave, valor in pessoa.items():
    print(chave, valor)

#args e kwargs
#args (já vimos)
#kwargs - kwargs arguments (argumento nomeados)

pessoa = {'nome': 'Aline',
          'sobrenome': 'Souza',}
          
dados_pessoa = {'idade': 15,
                'altura': 1.65}

pesso_completa = {**pessoa, **dados_pessoa}# dois **serve para juntas os dois dicionários
print(pesso_completa)
#desempacotamento de um dicionário ^^^^^^^

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)