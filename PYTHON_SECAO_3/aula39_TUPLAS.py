"""
tipo tuplas - uma lista imutavel
"""
#sempre que quiser fazer uma lista que nao vai precisar mudar
#nada dela fazer um tupla
# lista usa colchete [ ]
# tupla usa sem nada ou parenteses ( ) 

nomes = 'maria', 'helena', 'luiz'
print(nomes)
####################################
#converter lista para tupla e tupla para lista
nomes = ['maria', 'joao', 'luiz']
nomes = tuple(nomes) #converti para tupla
nomes= list(nomes) #converti para lista
print(nomes)