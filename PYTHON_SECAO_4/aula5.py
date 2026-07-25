"""
Higher Order Functions
Funções de primeira classe
"""
#as funções em python podem ser tratadas como qualquer outro tipo de dado

#não é muito comun usar print dendro de alguma função

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

print(executa(saudacao, 'Bom dia', 'Luiz'))
print(executa(saudacao, 'Boa tarde', 'Maria'))