"""
Formatação básica de strings
s - string
d - int
f - float
.<numero de digitos>f
x ou X hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
sinal - + ou -
ex.: 0>-100,.1f
conversion flags - !r !s !a
"""
variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
#<>^ esses comandos servem para centralizar ou 
#para esquerda ou direita 
print(f'{1000.83893893893: .1f}')