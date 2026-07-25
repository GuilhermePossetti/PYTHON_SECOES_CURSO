"""
closures em python

Ocorrem quando função internas, definidas dentro de outras funções refereciam
variáveis livres de seu escopo. Variáveis livres são as variáveis que não foram definidas
no escopo da função interna (são função externa)

Se a função externa retornar apenas a referência da função interna, então o interpretador
precisará atrelar quaisquer referências a variáveis livres que a função interna precisar para que 
ela possa ser executada corretamente
São muito usados em programação funcional, decoradores de função e algoritmos em geral

QUANDO VAMOS USAR CLOSURES

Para manter estados simples sem usar classes
Para criar fábricas (factories) de função
Para encapsular o código e esconder nomes importantes de escopos amplos
Para usar funções de callback (onde algo é feito por etapas)
Para decoradores de função em Python
Para programação funcional e algoritimos em geral
"""