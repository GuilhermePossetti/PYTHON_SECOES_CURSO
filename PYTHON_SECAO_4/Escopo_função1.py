"""
Escopo de funções em python
Escopo significa o local inde aquele codigo pode atingir
Existe o escopo global e local
O escopo global é o escopo onde todo o código é alcançavel
o escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados
"""
x = 1#que faz: cria/atribui a variável x no escopo global (módulo) com valor 1.

def escopo():#define a função escopo. A definição não executa o corpo; apenas cria o objeto função e o associa ao nome escopo no escopo global.
    global x#sso declara que todas as referências a x dentro de escopo referem-se à variável global (módulo), não a uma variável local.
    x = 10#dentro de escopo: quando escopo() for chamada, essa atribuição modifica a variável global x, trocando seu valor para 10.

    def outra_funcao():
        global x
        x = 11            #essa é outra função que faz a msm coisa q a primeira
        y = 2
        print(x, y)
    
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)

"""
Quando uma função está dentro de outra função, a lógica é que a função interna só existe dentro do
escopo da função externa — ela é criada quando a externa é executada e desaparece quando termina.
A função interna pode acessar variáveis da função externa, mas, por padrão, não pode modificá-las, a 
menos que use nonlocal (para variáveis da função de fora) ou global (para variáveis globais).
Essa estrutura é usada para organizar o código, isolar partes da lógica e criar funções auxiliares 
que só fazem sentido dentro de outra. Cada função tem seu próprio escopo local, com variáveis independentes 
das demais.
"""