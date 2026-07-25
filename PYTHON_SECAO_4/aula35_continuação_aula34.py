"""Funções decoradoras e decoradores
Decorar = Adicionar / Remover / Restringir / Alterar
Funções decoradoras são funções que decoram outras funções
Decoradores são usados para fazer o Python usar as funções
decoradoras em outras funções

Decradores são "syntax Sugar" (açúcar sintático)
"""

#                  OBSERVAÇÕES E ANOTAÇÕES

"""
@cria_funcao 

Isso é a forma oficial de usar decorators em Python.
Essa linha é apenas um atalho sintático para isto:

Ou seja, o Python faz automaticamente:
cria a função inverte_string
passa essa função para cria_funca
o decorator retorna interna
inverte_string passa a apontar para interna
"""

def cria_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg) #Aqui você chama a função e_string. Ela verifica se o argumento é uma string.
        resultado = func(*args, **kwargs)
        resultado += 'QUAL'
        print(f'Oseu resultado foi {resultado}')
        print('Ok, agr vc foi decorada')
        return resultado
    return interna

@cria_funcao
def inverte_string(string):
    return string[:: -1]

def e_string(param):#Função para validar o tipo do parâmetro.
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string')
    
invertida = inverte_string('123')
print(invertida)