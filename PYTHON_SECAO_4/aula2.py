"""
Argumentos NOMEADOS e NÃO NOMEADOS em função Python
Argumentos NOMEADOS tem nome com sinal de igual
Argumentos NÃO NOMEADOS recebe apenas o argumento (valor)
"""

#Definição
def soma(x, y): #parametro vem na definição da função e o parametro é a variavel
    print(f'{x=} {y=}', '|', 'x + y = ', x + y)

soma(1, 2)#ele esta passando o argumento 1 para X e argumento 22 para Y
soma(y=2, x=1)#ultilizou argumentos nomeados para escolher os numero fora de ordem
#a partir do momento em que foi renomeado um parametro, todos os que vierem dps precisam estar nomeado
# dica, deixa tudo nomeado ou nao deixa nenhum nomeado

#argumento é o valor que eu passo para a variavel Argumentos NOMEADOS ou Argumentos NÃO NOMEADOS