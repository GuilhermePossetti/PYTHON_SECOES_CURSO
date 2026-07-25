"""
Escopo de funções em python
Escopo significa o local inde aquele codigo pode atingir
Existe o escopo global e local
O escopo global é o escopo onde todo o código é alcançavel
o escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados
Não temos acesso a nomes de escopos internos nos escopos externos
A palavra global faz variavel do escopo externo
ser a mesma no escopo interno 
"""

x = 1

def escopo():
    global x #pode usar o global mas isso é MÁ PRATICA
    x = 10

    def outra_funcao():
        global x #pode usar o global mas isso é MÁ PRATICA
        x = 11  
        y = 2          
        print(x, y)
    
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)
