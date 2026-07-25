""" Calculadora com while """
while True:  # loop infinito, só para quando der um break
    numero_1 = input('Digite um número: ') # lê o primeiro número (string)
    numero_2 = input('Digite outro número: ')  # lê o segundo número (string)
    operador = input('Digite o operador (+-/*): ')  # lê o operador matemático

    numeros_validos = None# variável para indicar se os números são válidos

    try:# tenta converter os números para float
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True# se der certo, marca como válidos
    except:
        numeros_validos = None# se der erro, números são inválidos

    if numeros_validos is None:# checa se houve erro na conversão
        print('Um ou ambos os números digitados são inválidos.')
        continue# volta para o início do loop

    operadores_permitidos = '+-/*'# define os operadores aceitos

    if operador not in operadores_permitidos: # verifica se operador é válido
        print('Operador inválido.')
        continue# volta para o início do loop

    if len(operador) > 1:# impede que digitem mais de um operador
        print('Digite apenas um operador.')
        continue # volta para o início do loop

    print('Realizando sua conta:')# mensagem antes do cálculo
# executa a operação escolhida
    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
# pergunta se o usuário deseja sair
    sair = input('Quer sair? [s]im: ').startswith(('s' , 'S'))
# se começar com 's' ou 'S'
    if sair is True:
        break# sai do loop e encerra o programa