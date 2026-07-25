"""
Closures em python 
O que são closures?
ocorrem quando funções internas definidas dentro de outra funções
referenciam variáveis livres do seu escopo. Variávies livres são as
variáveis que não foram definidas no escopo da função interna(são função externa)
se a função externa retornar apenas a referência da função interna, então 
o interpretador precisará atrelar quaisquer referência a variáveis livres
que a função interna precisar para que ela possa ser executada corretamento
são muito usados em programação funcional, decoradores de função e algoritimos em geral
"""