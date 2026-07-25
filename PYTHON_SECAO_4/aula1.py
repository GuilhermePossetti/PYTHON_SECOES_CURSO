"""
introdução as funções (def) em Python
funções são trechos de códigos udados para replicar determinada
ação ao longo do seu código
elas podem receber valores para parâmetro (argumentos)
e retornar um valor específico
por padrão funções retorna None (nada)
"""
# para definir uma função 

# def  saudacao(nome):
#     print(f'Olá, {nome}!')

# saudacao('Guilherme')
# saudacao('Sabrina')

"""
def saudacao(nome):
def é a palavra-chave que define (declara) uma função em Python.
saudacao é o nome da função (o identificador que você usa para chamá-la).
(nome) é a lista de parâmetros — aqui a função espera um argumento chamado nome.
: indica o início do bloco da função; todo o código indentado abaixo pertence à função.
print(f'Olá, {nome}!')
Está indentado — pertence ao corpo da função saudacao.
print(...) é a função built-in que envia texto para a saída padrão (normalmente o terminal).
f'Olá, {nome}!' é uma f-string (string literal formatada). O {nome} é substituído pelo valor do parâmetro nome quando a linha é executada.
Se nome for 'Guilherme', a string avaliada será 'Olá, Guilherme!'.
saudacao('Guilherme')
Aqui você chama (invoca) a função saudacao e passa a string 'Guilherme' como argumento.
Ao executar, o Python entra na função, atribui 'Guilherme' ao parâmetro nome e executa o print, mostrando Olá, Guilherme! no console.
"""

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)

multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)
 