"""
Métados úteis dos dicionários em PY
len - quantas chaves
keys - iteraveis com chaves
values - iteravel com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
"""

pessoa = {
    'nome' : 'Gui',
    'sobrenome' : 'Po7',
}

print(len(pessoa)) #retorna qnts palavras tem dentro das chaves
print(pessoa.keys()) #retorna os valores das chaves ex: 'nome' e 'sobrenome'

##################################################################################

d1 = {
    'c1' : 1,
    'c2' : 2,
    'l1' : [0, 1, 2],
}
d2 = d1.copy()
                                  #copia raza
d2['c1'] = 4000
d2['l1'][1] = 520022

print(d1)
print(d2)

########################################################################################

p1 = { 
    'nome' : 'Gui',
    'sobrenome' : 'Po7',   #mostra o valor de uma chave desejada
}
print(p1.get('nome'))

#########################################################################################

p1 = { 
    'nome' : 'Gui',
    'sobrenome' : 'Po7',
}                                  #exclui uma chave
nome = p1.pop('nome')
print(nome)
print(p1)

##########################################################################################

p1 = { 
    'nome' : 'Gui',
    'sobrenome' : 'Po7',
}

p1.update({
    # 'nome' : 'novo valor',     #altera a chave desejada ou adiciona alguma coisa
    # 'idade' : 50,
    #  ou dessa forma  #
    p1.update(nome='novovalor', idade=80) 
})
print(p1)