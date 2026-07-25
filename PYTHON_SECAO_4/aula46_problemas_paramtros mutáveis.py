# Problema dos parâmetros mutáveis em funções Python

def adiciona_clientes(nome, lista=[]):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('fernandoi', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente2)
print(cliente2)

