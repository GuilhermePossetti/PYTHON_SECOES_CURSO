"""
Sets - Conjuntos em Py (tipo set)
Conjuntos são ensinados na matemática
https://brasilescola.uol.com.br/matematica/conjunto.htm
Representados graficamente pelo diagrama de Venn
Sets em Py são mutáveis, porém aceitam apenas
tipos imutáveis como valor interno

Criando um set
Set(iterável) ou {1, 2, 3}


Sets são eficantes para remover valores duplicados de iteváveis
- eles não tem índexes;
- eles não garantem ordem;
- eles são iteráveis (for, in, not in)

Métados úteis: add, update, clear, discard
"""

s1 = set() #set vazio
s1 =set('Guilherme', 1, 2, 3) #set com dados

#Sets remove valores repetidos
s2 = {1, 1, 2, 3, 3, 4, 4, 8, 10, 10, 5, 5,}
print(s2)

s3 = {1, 2, 3}
print(3 in s3)
      #ou#
for numero in s3:
    print(numero)

########Métados úteis: add, update, clear, discard#########
s1 = set() #cria um set vazio
s1.add('Gui') #adiciona um único elemento ao set valor adicionado (string)
s1.add(1) #Adiciona o número 1 ao set Set pode ter tipos diferentes (string, int, etc.)
s1.update(('Olá mundo', 1, 2, 3,)) #adiciona vários valores de uma vez () → isso é uma tupla O 1 já existe, então o set ignora Set não duplica valores
s1.clear() #remove tudo do set Deixa ele completamente vazio
s1.discard('Olá mundo') #tenta remover um valor do set
print(s1)

"""
Operadores úteis:
união | união (union) - une
intersecção & (intersection) - Itens presentes em ambos
diferença - Itens presentes apenas no set da esquerda
diferença simétrica ^ - Itens que não estão em ambos
"""
s1 = {1, 2, 3,} #Cria um set
s2 = {2, 3, 4,} #Cria um set
s3 = s1 | s2 #União = junta tudo sem repetir
s3 = s1 & s2 #Interseção = só o que existe nos dois
s3 = s1 - s2 #Diferença = o que está em s1 mas não em s2
s3 = s1 ^ s2 #Diferença simétrica = o que está em um ou outro, mas não nos dois
print(s3)

############### EXEMPLO DE USO DOS SETS #########################

letras = set()
while True:
    letra = input('Letra: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('parabens')
        break
    print(letras)