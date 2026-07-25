"""
Funções decoradoras e decoradores
Decorar = Adicionar / Remover / Restringir / Alterar
Funções decoradoras são funções que decoram outras funções
Decoradores são usados para fazer o Python usar as funções
decoradoras em outras funções
"""#               OBSERVAÇÕES E ANOTAÇÕES
 
#                  OBSERVAÇÕES E ANOTAÇÕES
                  
"""                OBSERVAÇÕES E ANOTAÇÕES

def → cria uma função.
cria_funca → nome da função decoradora.
func → parâmetro que recebe outra função.

interna é a função que vai substituir a função original.
*args → recebe vários argumentos posicionais.
**kwargs → recebe argumentos nomeados.

for arg in args: PERCORRE TODOS OS ARGUMENTOS RECEBIDOS
O LOOP FARIA: arg = "a"
              arg = "b"
              arg = "c"

resultado = func(*args, **kwargs) 
func é a função original que foi passada.
"cria_funca(inverte_string)"  , "func = inverte_string'
Então essa linha executa: inverte_string(*args, **kwargs)
Exemplo real: inverte_string('123') Resultado: '321'

f-string → permite colocar variáveis dentro do texto.

return resultado:
Aqui o decorator devolve o resultado da função original.
Se você não retornasse isso, o resultado seria None

return interna Isso é o ponto principal do decorator.
A função cria_funca não retorna o resultado, ela retorna uma nova função.
Ou seja: cria_funca(inverte_string)
vira: interna

return string[::-1] = Esse é um slice do Python.

[::-1] = percorrer a string de trás para frente

isinstance() verifica o tipo do objeto.

raise em Python significa “lançar” ou “gerar” uma exceção (erro).
Ou seja, você usa raise quando quer interromper a execução do programa e avisar que ocorreu um erro
"""
def cria_funca(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg) #Aqui você chama a função e_string. Ela verifica se o argumento é uma string.
        resultado = func(*args, **kwargs)
        print(f'Oseu resultado foi {resultado}')
        print('Ok, agr vc foi decorada')
        return resultado
    return interna

def inverte_string(string):
    return string[:: -1]

def e_string(param):#Função para validar o tipo do parâmetro.
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string')
    
inverte_string_checando_parametro = cria_funca(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)

