# """
# interpolação basica de strings
# s - string
# d e i - int
# f - float
# x e x - Hexadecimal (ABCDEF0123456789)
# """
# interpolação é usar %e alguma letra de S string F float para "adiantar"
nome = 'guilherme'
preco = 1000.95897643
variavel = '%s, o preço é: R$%.2f' % (nome, preco) #interpolação
print(variavel)
print('o hexadecimal de %d é %04x' % (15, 5))
# %d é a interpolação de inteiro
# %04x é a interpolação do hexadecimal
# o numero 04 antes do x é para dizer qnts casas decimais

