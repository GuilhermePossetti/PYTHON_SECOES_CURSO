"""
Flag (bandeira) - marcar um local
none = não valor
is e is not = é ou não é(tipo, valor idebtidade)
id = identidade
"""
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('faca algo')
else:
    print('nao faca algo')


if passou_no_if is None:
    print('n passou no if')

if passou_no_if is not None:
    print('passou no if')    