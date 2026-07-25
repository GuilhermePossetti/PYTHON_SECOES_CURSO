"""
Valores padrão para parâmetros  
Ao definir uma função, os parâmetros podem ter valores
padrão, Caso o valor NÃO SEJA enviado para o parâmetro
o valor padrão SERÁ USADO

Refatorar: editar o seu código

"""

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', '|', x + y + z)
    else:
        print(f'{x=} {y=}', '|', x + y)

soma(1, 2)
soma(4, 5)
soma(100, 200)
soma(15, 20, 50)