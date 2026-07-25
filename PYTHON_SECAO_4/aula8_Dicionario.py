# Manipulando chaves e valores em dicionários

pessoa = {} #Cria um dicionário vazio chamado pessoa

##
##

chave = 'nome' #Cria uma variável chamada chave. Ela guarda a string 'nome'

#Isso é importante porque a chave do dicionário será definida dinamicamente, usando uma variável.

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'

#cria a chave com os valores

print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']  #Remove a chave 'sobrenome' do dicionário
print(pessoa)
print(pessoa['nome'])

print(pessoa.get('sobrenome')) #.get() tenta acessar a chave 'sobrenome'
if pessoa.get('sobrenome') is None: #Verifica se a chave 'sobrenome' não existe.
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

print('ISSO Não vai')

"""
Como criar um dicionário
Como adicionar chaves
Como alterar valores
Como remover chaves (del)

O dicionário representa uma estrutura de dados dinâmica
onde os valores são acessados por chaves
"""


