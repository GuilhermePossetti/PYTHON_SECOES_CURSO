"""
cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['luiz', 'maria', 1, True, 1.2]
lista_b = lista_a.copy()#copiar a lista

lista_a[0] = 'qualquer coisa'
print(lista_a)
print(lista_b)