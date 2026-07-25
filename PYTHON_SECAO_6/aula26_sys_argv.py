# sys.argv - Executando arquivo com argumentos no sistema
# Fonte = Fira Code

import sys

argumentos = sys.argv
qtd_arguentos = len(argumentos)

if qtd_arguentos <= 1:
    print('Vc n passou arg')
else:
    try:
        print(f'Vc passou arg {argumentos[1:]}')
        print(f'faz alg coisa com {argumentos[1:]}')
        print(f'faz otra coisa  com {argumentos[1:]}')
    except IndexError:
        print('flta args')