"""
Dicionário de python (tipo dict)
São estruturas de dados do tipo par de "chave" e "valor"
chaves podem ser consideradas como "índice" que vimos na lista e podem ser de tipos imutáveis
como: STR, INT, FLOAT, BOOL, TUPLE, ETC...
o valor pode ser de qualquer tipo, incluindo outro dicionário
usamos as chaves {} ou a classe dict para criar dicionários 

imutáveis: STR, INT, FLOAT, BOOL, TUPLE
mutáveis: dict, list
"""
pessoa = {
    'nome' : 'Gui',
    'sobrenome' : 'Po7',
    'idade' : '21',
    'altura' : '1.75', 
    'endereços' : [
        {'rua' : 'TAL, TAL, TAL', 'numero' : '600'},
        {'rua' : 'outra rua', 'numero' : '75'},

    ]
}
print(pessoa, type(pessoa))

print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])