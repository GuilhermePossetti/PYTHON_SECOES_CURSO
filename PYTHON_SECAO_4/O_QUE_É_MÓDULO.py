"""
Um módulo é basicamente um arquivo .py com código dentro 
que pode ser reutilizado em outro arquivo.

Ele serve para: Organizar o código
                Reaproveitar funções
                Evitar repetir código
                Separar responsabilidades (boa prática de Engenharia de Software 😉)

Exemplo:

arquivo: meu_modulo.py
    def soma(a, b):
        return a + b

arquivo principal: main.py
    import meu_modulo
        print(meu_modulo.soma(2, 3))

Aqui:   meu_modulo é o módulo
        soma é uma função dentro do módulo
        Para acessar → meu_modulo.soma()

FORMAS DE IMPORTAR UM MÓDULO 
1️⃣ Importando tudo:  import sys
USA ASSIM: sys.exit()

2️⃣ Importando algo específico: from sys import exit
USA ASSIM: exit()

3️⃣ Dando apelido: import sys as s
USA ASSIM: s.exit()

//////////////////////////#######################/////////////////////////


🧠 MÓDULO sys

O módulo sys é um módulo interno do Python (já vem instalado).
Ele permite interagir com o interpretador Python e com o sistema.

Muito usado: sys.exit():
                            import sys
                            print("Antes de sair")
                            sys.exit()
                            print("Isso nunca será executado")

Quando executa sys.exit():
➡ O programa é encerrado imediatamente.


**  Muito usado: sys.exit(), sys.argv, sys.path
** sys é um módulo interno
** sys interage com o sistema/interpretador


MÓDULO __main__

A palavra main significa: principal ou ponto de entrada do programa

É o arquivo ou parte do código onde a execução começa.

main significa principal, sendo usado como ponto de entrada do programa. 
Em Python, utiliza-se a verificação if __name__ == "__main__" para garantir que 
determinado código seja executado apenas quando o arquivo for rodado diretamente, 
e não quando for importado como módulo.
"""
print('Só testando')