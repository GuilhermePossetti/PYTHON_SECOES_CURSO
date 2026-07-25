#         ###################################
# ######## exercício de soma e média escolar ##########
#         ###################################

try:#executa tudo oq esta dentro dele, se caso der erro em alguma coisa, nada q esta dentro dele executa, e pula direto para o except
    nota_1 = float(input('Digite sua primeira nota: '))#pergunta para o usuario suas notas, em float para pessoa poder usar . ou ,
    nota_2 = float(input('Digite sua segunda nota: '))#pergunta para o usuario suas notas, em float para pessoa poder usar . ou ,
    nota_3 = float(input('Digite sua terceira nota: '))#pergunta para o usuario suas notas, em float para pessoa poder usar . ou ,

    media = (nota_1 + nota_2 + nota_3) / 3 #faz a media da nota soma as nota e o resultado divide pelo tanto de nota
    print(f'{media:.2}')#mostra o resultado da média mas so com duas casa dps da virgula

    if media >= 7:# se a media for maior ou igual a seta
        print('Aprovado')#aparece para  usuasrio isso

    elif media in range(5, 7):#se não se media estiver entre 5 e 7 
        print('Recuperação')##aparece para  usuasrio isso

    elif media <= 5:#se não a media for menor ou igual a 5 
        print('Reprovado')#aparece para  usuasrio isso

except:#se cado o try der algum erro pula direto pra ca e encerra o codigo
    print('Digite apenas números')#aparece para  usuasrio isso


#                  ####################
#          ######## exercício de idade ##########
#                  ####################

try:#executa tudo oq esta dentro dele, se caso der erro em alguma coisa, nada q esta dentro dele executa, e pula direto para o except
    ano_nascimento = int(input('Digite o ano do seu nascimento: '))#pede para o usuario digitar o ano do seu nasciemnto, o int serve para valores sem virgula
    idade = 2025 - ano_nascimento#conta para qualcular a idade ano atual - ano nasciemnto
    print(f'{idade}')#aparece para  usuasrio isso, f de str

    if idade <= 12:#se idade for menor ou igual a 12
        print('Criança')#aparece para  usuasrio isso
    elif idade in range(12, 17):#se não se idade estiver entre 12 e 17
        print('Adolecente')#aparece para  usuasrio isso
    elif idade in range(18, 64):#se não se idade estiver entre 18 e 64
        print('Adulto')#aparece para  usuasrio isso
    elif idade >= 65:#se idade for maior ou igual a 65
        print('Idoso')#aparece para  usuasrio isso
except:#se cado o try der algum erro pula direto pra ca e encerra o codigo
    print('Digite apenas seu ano de nascimento')#aparece para  usuasrio isso


#            #####################################
#     ######## exercício de somar o IMC corporal ##########
#             ####################################

nome = 'guilherme' #str nome, varialvel tipo string nome
altura = 1.75#float altura, varialvel tipo float altura
peso = 109#int peso, varialvel tipo int peso
imc = peso / (altura * altura)#conta para calcular o IMC, altura * altura dps divide pelo peso
print('seu imc é:', imc)#aparece para  usuasrio isso


#        ######################################################
#     ######## exercício para ver qual valor é maior ou igual ##########
#             #################################################

primeiro_valor = input('Digite um valor: ')#Aqui você está pedindo ao usuário que digite algo.
segundo_valor = input('Digite outro valor: ')#Mesma coisa que a linha anterior, só que agora estamos pegando outro valor do usuário.

if primeiro_valor > segundo_valor:#if verifica se o primeiro_valor é maior que o segundo_valor.
    print('Primeiro valor é maior que o segundo valor.')#aparece para  usuasrio isso

elif primeiro_valor == segundo_valor:#elif significa “senão, se”.Aqui verificamos se os dois valores são iguais.Se forem iguais, imprime a mensagem de igualdade.
    print('Os dois valores são iguais.')#aparece para  usuasrio isso

else:#else significa “caso nenhuma das condições anteriores seja verdadeira”.Ou seja, se o primeiro valor não for maior e não for igual, então o segundo é maior.
    print('Segundo valor é maior que o primeiro valor.')#aparece para  usuasrio isso


#            #############################################################
#     ######## exercício para digitar seu nome, ivertido, espaço, letras ##########
#             ############################################################

nome = input('Digite seu nome: ')#Aqui você está pedindo que o usuário digite o nome e a idade.
idade = input('Digite sua idade: ')#Aqui você está pedindo que o usuário digite o nome e a idade.

if nome and idade:#Esse if verifica se os dois campos não estão vazios.Se a pessoa digitou algo em nome e idade, entra no bloco if.Se algum dos dois estiver vazio, vai para o else.
    print(f'Seu nome é:{nome}')#f'...' é uma f-string, que permite colocar variáveis dentro da string usando {}
    print(f'Seu nome invertido é: {nome[::-1]}')#{nome[::-1]} inverte a string.

    if ' ' in nome:#Aqui você verifica se o nome contém espaço.' ' in nome → retorna True se houver pelo menos um espaço no nome.
        print('Seu nome TEM espaço. ')##aparece para  usuasrio isso
    else:#se o nome nao tiver espaço o else vai executar
        print('Seu nome NÃO tem espaço. ')##aparece para  usuasrio isso

    print(f'Seu nome tem {len (nome)} letras')#len(nome) retorna quantos caracteres o nome tem, incluindo espaços.
    print(f'A primeira letra do seu nome é: {nome[0]}')#nome[0] → primeira letra do nome
    print(f'A última letra do seu nome é: {nome[-1]}')#nome[-1] → última letra do nome (o -1 indica o último índice)

else:#Se nome ou idade estiverem vazios, o programa mostra essa mensagem de erro.
    print('Desculpe, você deixou campos vazios.')#aparece para  usuasrio isso


#            #########################
#     ######## exercício CALCULADORA ##########
#            #########################

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
    if operador == '+':#Aqui verificamos se a variável operador contém o símbolo '+' Se for '+', o Python soma os dois números (num_1_float + num_2_float) e mostra o resultado com print().
        print(num_1_float + num_2_float)#mostra a soma
    elif operador == '-':#elif significa “senão, se”.Se o operador for '-', o Python subtrai o segundo número do primeiro e mostra o resultado.
        print(num_1_float - num_2_float)#mostra a subtração
    elif operador == '*':#Se o operador for '*', o Python multiplica os dois números.
        print(num_1_float * num_2_float)#mostra a multiplicação
    elif operador == '/':#Se o operador for '/', o Python divide o primeiro número pelo segundo.
        print(num_1_float / num_2_float)#mostra a divisão
# pergunta se o usuário deseja sair
    sair = input('Quer sair? [s]im: ').startswith(('s' , 'S'))
# se começar com 's' ou 'S'
    if sair is True:
        break# sai do loop e encerra o programa


#            #########################
#     ######## exercício CAÇA-PALAVRA ##########
#            #########################

import os #O os permite executar comandos do sistema operacional
#como limpar a tela com os.system('cls').

palavra_secreta = 'gui'#Define a palavra que o jogador precisa adivinhar.
letras_acertadas = ''#Cria uma string vazia para guardar as letras que o jogador acertou.
numero_tentativas = 0#Inicializa um contador para quantas tentativas o jogador fez.

while True:#Inicia um loop infinito, que vai repetir até a palavra ser completada.
    letra_digitada = input('Digite uma letra: ')#Pede ao jogador que digite uma letra
    numero_tentativas += 1#Cada vez que o jogador digita, incrementa o número de tentativas.

    if len(letra_digitada) > 1:#Verifica se o jogador digitou mais de uma letra.
        print('Digite apenas uma letra.')#Se sim, mostra a mensagem e continue faz o loop pular o restante do código e voltar para o input.
        continue#se iss ofor verdadeiro ele volta para o input(digite uma letra) para começar de novo

    if letra_digitada in palavra_secreta:#Se a letra digitada estiver na palavra secreta, ela é adicionada à string
        letras_acertadas += letra_digitada#letras_acertadas.

    palavra_formada = ''#Cria a palavra que vai aparecer na tela (palavra_formada):
    for letra_secreta in palavra_secreta:#Percorre cada letra da palavra secreta.
        if letra_secreta in letras_acertadas:#Se a letra já foi acertada, adiciona ela a palavra_formada.
            palavra_formada += letra_secreta
        else:#Se não
            palavra_formada += '*'#adiciona um '*' no lugar (oculta a letra).

    print('Palavra formada:', palavra_formada)#Mostra ao jogador como está a palavra com as letras acertadas e os asteriscos.

    if palavra_formada == palavra_secreta:#Verifica se a palavra formada já é igual à palavra secreta.Se sim:
        os.system('cls')#Limpa a tela (os.system('cls') no Windows)
        print('VOCÊ GANHOU!! PARABÉNS!')#Mostra mensagem de vitória
        print('A palavra era', palavra_secreta)#Mostra a palavra secreta 
        print('Tentativas:', numero_tentativas)#e quantas tentativas o jogador fez
        letras_acertadas = ''#Reseta letras_acertadas
        numero_tentativas = 0#numero_tentativas para jogar de novo


#            #####################################################
#     ######## exercício de verificar se oCPF VÁLIDO ou INVÁLIDO ##########
#            #####################################################

# """
# Calculo do segundo dígito do CPF
# CPF: 746.824.890-70
# Colete a soma dos 9 primeiros dígitos do CPF,
# MAIS O PRIMEIRO DIGITO,
# multiplicando cada um dos valores por uma
# contagem regressiva começando de 11

# Ex.:  746.824.890-70 (7468248907)
#    11 10  9  8  7  6  5  4  3  2
# *  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
#    77 40 54 64 14 24 40 36  0 14

# Somar todos os resultados:
# 77+40+54+64+14+24+40+36+0+14 = 363
# Multiplicar o resultado anterior por 10
# 363 * 10 = 3630
# Obter o resto da divisão da conta anterior por 11
# 3630 % 11 = 0
# Se o resultado anterior for maior que 9:
#     resultado é 0
# contrário disso:
#     resultado é o valor da conta

# O segundo dígito do CPF é 0
# """

# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
import re#importa a biblioteca expressões regulares, usada para manipular e filtrar strings.
import sys#importa o módulo sistema, que permite, por exemplo, encerrar o programa com sys.exit().

cpf_enviado_usuario = '746.824.890-70'.replace('.', '').replace('-', '')
#primeira aspas serve para mostra oq tirar e a outra oq colocar

entrada = input('CPF [746.824.890-70]: digite um cpf: ')
cpf_enviado_usuario = re.sub(r'[^0-9]','', entrada)
#essa linha e esse comando import re re.sub r'[^algum numero]', '', e o cpf
#serve para tirar qualquer coisa que n seja numero
entrada_e_sequencial = entrada == entrada[0] * len(entrada)#Verifica se o CPF digitado é sequencial, tipo '11111111111'.
#Se for igual à entrada, significa que todos os números são iguais → CPF inválido.
if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()#encerra o programa
#Se for sequencial, mostra mensagem de erro e encerra o programa.
nove_digitos = cpf_enviado_usuario[:9]#Pega os primeiros 9 dígitos do CPF, que serão usados para calcular o primeiro dígito verificador.
contador_regressivo_1 = 10#contador_regressivo_1 = 10 → contador usado na multiplicação regressiva.

resultado_digito_1 = 0#Cria uma variável chamada resultado_digito_1 e inicializa com 0.Ela vai guardar a soma dos produtos de cada dígito pelo contador regressivo.
for digito in nove_digitos:#Esse for percorre cada caractere da string nove_digitos Cada caractere é armazenado temporariamente na variável digito.Exemplo: se nove_digitos = '746824890', o loop vai pegar: '7', depois '4', '6' e assim por diante.
    resultado_digito_1 += int(digito) * contador_regressivo_1#int(digito) → converte a letra (ex: '7') para número (7).Multiplica esse número pelo contador regressivo (contador_regressivo_1).resultado_digito_1 += ... → soma esse resultado à variável que guarda a soma total.
    contador_regressivo_1 -= 1#Decrementa o contador em 1 a cada passo do loop. Isso faz com que o multiplicador vá decrescendo de 10 para 9, 8, 7… até 2, como exige a regra de cálculo do CPF.
digito_1 = (resultado_digito_1 * 10) % 11#Calcula o primeiro dígito verificador do CPF.(resultado_digito_1 * 10) % 11 → fórmula oficial do CPF.
digito_1 = digito_1 if digito_1 <= 9 else 0#Se o resultado for maior que 9, define digito_1 = 0

dez_digitos = nove_digitos + str(digito_1)#Junta os 9 dígitos originais + o primeiro dígito verificado
contador_regressivo_2 = 11#Prepara o contador regressivo para calcular o segundo dígito verificador (começa em 11).

resultado_digito_2 = 0##Cria uma variável chamada resultado_digito_1 e inicializa com 0.Ela vai guardar a soma dos produtos de cada dígito pelo contador regressivo.
for digito in dez_digitos:##Esse for percorre cada caractere da string nove_digitos Cada caractere é armazenado temporariamente na variável digito.Exemplo: se nove_digitos = '746824890', o loop vai pegar: '7', depois '4', '6' e assim por diante.
    resultado_digito_2 += int(digito) * contador_regressivo_2##int(digito) → converte a letra (ex: '7') para número (7).Multiplica esse número pelo contador regressivo (contador_regressivo_1).resultado_digito_1 += ... → soma esse resultado à variável que guarda a soma total.
    contador_regressivo_2 -= 1##Decrementa o contador em 1 a cada passo do loop. Isso faz com que o multiplicador vá decrescendo de 10 para 9, 8, 7… até 2, como exige a regra de cálculo do CPF.
digito_2 = (resultado_digito_2 * 10) % 11#Calcula o primeiro dígito verificador do CPF.(resultado_digito_1 * 10) % 11 → fórmula oficial do CPF.
digito_2 = digito_2 if digito_2 <= 9 else 0#Se o resultado for maior que 9, define digito_1 = 0


cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'#Junta os 9 dígitos + primeiro dígito + segundo dígito em uma string.
#Esse é o CPF calculado pelo Python a partir da fórmula oficial.
if cpf_enviado_usuario == cpf_gerado_pelo_calculo:#Compara o CPF digitado pelo usuário com o CPF gerado pelo cálculo.
    print(f'{cpf_enviado_usuario} é válido')#saida resultado
else:#Se forem diferentes
    print('CPF inválido')#CPF inválido.


#                #########################################
#         ######## exercício para geral 10 cpf diferente ##########
#                #########################################

import random

for _ in range(10):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    contador_regressivo_1 = 10
    resultado_digito_1 = 0
    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11

    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    print(cpf_gerado_pelo_calculo)


               ####################################################               
        ######## exercício interpretador, docstring, comentarios  ##########
               ####################################################
"""
Este programa foi feito para realizar a soma de dois números.
O usuário digita dois valores e o programa mostra o resultado da soma.
"""
# Entrada de dados (usuário digita dois números)
numero = float(input('Digite um numero: '))
numero_11 = float(input('Digite outro numero: '))

# Processamento (soma dos números digitados)
soma = numero + numero_11

# Saída de dados (mostra o resultado na tela)
print('A soma deles é', soma)



               ##################################               
        ######## exercício Calculadora Simples  ##########
               ##################################
"""
Calculadora Simples
Este programa permite ao usuário escolher uma operação matemática básica
(soma, subtração, multiplicação ou divisão), digitar dois números e ver o resultado.
"""
print('Escolha uma das opções abaixo')

print('soma [1]')
print('subtração [2]')
print('multiplicação [3]')
print('divisão [4]')


while True:
    try:
        numero_escolhido = int(input('Digite uma opção há cima: '))
        if numero_escolhido not in [1, 2, 3, 4]:
            print('Digite apenas umas dessa opções')
            continue

        numero_1 = float(input('Agora digite um numero: '))
        numero_2 = float(input('Digite outro numero: '))
            
        if numero_escolhido == 1:
            soma = numero_1 + numero_2
            print('A soma deles são: ', soma)
        elif numero_escolhido == 2:
            subtracao = numero_1 - numero_2
            print('A subtração deles são: ', subtracao)
        elif numero_escolhido == 3:
            multiplicacao = numero_1 * numero_2
            print('A multiplicação deles são: ', multiplicacao)
        elif numero_escolhido == 4:
            divisao = numero_1 / numero_2
            print('A divisão deles são: ', divisao)

        
        continuar = input('Deseja continuar? [s]im, [n]ão: ').strip()
        if continuar in ['Sim', 'sim', 's', 'S']:
            print('vamos de novo')
            continue
        elif continuar in ['Não', 'Nao', 'não', 'nao', 'n', 'N', 'Ñ', 'ñ']:
            print('Tchau')
            break
        else:
            print('Opção inválida')
            
    except ValueError:
        print('Obrigado')

                ##############################              
        ######## exercício Lista de Compras  ##########
               ###############################


print('Bem-vindo a lista de compra')

lista_de_compra = []

while True:

    print('\nEscolha uma das opções abaixo: ')
    print('Adicionar intem [1]: ')
    print('Ver lista [2]: ')
    print('Remover item da lista [3]: ')
    print('Sair [4]: ')

    opcao = int(input('Digite o numero que escolheu: '))

    if opcao == 1:
        item = input('O que deseja adicionar em sua lista? ')
        lista_de_compra.append(item)
        print(f'Adicionado a lista {item}')

    elif opcao == 2:
        if len(lista_de_compra) == 0:
            print('Lista Vazia')
        else:
            print('Itens da sua lista:')
            for i, item in enumerate(lista_de_compra, start=1):
                print(f'{item}, {i}')

    elif opcao == 3:
        if len(lista_de_compra) == 0:
            print('A lista esta fazia. Nada para remover.')
        else:
            item = input('Digite o que deseja remover?')
            if item in lista_de_compra:
                lista_de_compra.remove(item)
                print(f'Item removido', {item})
            else:
                print(f'não esta na lista', {item})

    elif opcao == 4:
        print('tchau')
        break

    else:
        print('Opção ivalida. digite 1 2 3 ou 4')


                          
               ##############################################              
        ######## exercício outra opção de Lista de Compras  ##########
               ##############################################
               


"""
faça uma lista de compra
o usuario deve ter a possibilidade de
inserit, apagar e listar algo da sua lista
"""
"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os #Aqui é usado para chamar os.system('cls') (executar um comando de shell para limpar a tela).

lista = [] #cria uma lista vazia chamada lista. Ela vai armazenar os valores inseridos pelo usuário. Em Python a lista é mutável: 
#você pode adicionar (append), remover (del), etc.

while True: #inicia um laço infinito. O bloco dentro desse while será repetido indefinidamente até que o programa seja encerrado
    print('Selecione uma opção') #Imprime a mensagem na tela
    opcao = input('[i]nserir [a]pagar [l]istar: ').lower() #mostra o prompt entre parênteses e lê o que o usuário digitar, retornando uma string

    if opcao == 'i': #Verifica se o usuário escolheu a opção 'i' (inserir). Se sim, executa o bloco seguinte
        os.system('cls')#Executa o comando de shell 'cls' (limpar tela)
        valor = input('Valor: ')#Pede ao usuário que digite o valor a ser inserido
        lista.append(valor)#Adiciona (append) o valor ao fim da lista lista. A lista cresce dinamicamente.
        
    elif opcao == 'a':#Se a opção não foi 'i' mas foi 'a' (apagar), executa o bloco abaixo.
        indice_str = input('Escolha o índice para apagar: ')#Pede ao usuário o índice do item que deseja apagar

        try:#Inicia um bloco try para capturar exceções que possam ocorrer durante a conversão do índice ou a remoção do elemento.
            indice = int(indice_str)#Tenta converter a string indice_str para um inteiro usando int(). Se o usuário digitar algo que não seja um inteiro válido
            del lista[indice]#Se indice estiver fora do intervalo válido (por exemplo len(lista) é 3 e indice for 5), Python levanta IndexError.
                                #Índices negativos funcionam (ex.: -1 remove o último elemento).
                                #Após del, os elementos à direita deslocam-se para a esquerda (índices são atualizados).   
        except ValueError:#Captura especificamente ValueError — que ocorre normalmente se int(indice_str) falhar (entrada não numérica).
            print('Por favor digite número int.')#Mensagem informando que o usuário deve digitar um número inteiro.
        except IndexError:#Captura IndexError — ocorre se del lista[indice] tentar remover um índice que não existe na lista.
            print('Índice não existe na lista')#Mensagem informando que o índice informado é inválido (fora do alcance da lista).
        except Exception:#Captura qualquer outra exceção que herde de Exception. É um except genérico para tratar erros não previstos
            print('Erro desconhecido')#Mensagem genérica quando cai no except Exception
    elif opcao == 'l':#Se a opção foi 'l' (listar), executa o bloco seguinte.
        os.system('cls')#Limpa a tela novamente (mesma observação de portabilidade — funciona no Windows).

        if len(lista) == 0:#Verifica se a lista está vazia. len(lista) retorna o número de elementos na lista.
            print('Nada para listar')#Se a lista estiver vazia, informa ao usuário que não há nada a mostrar.

        for i, valor in enumerate(lista):#Percorre a lista com enumerate, que retorna pares (índice, valor) para cada item
            print(i, valor)#Imprime o índice e o valor separados por um espaço (com o comportamento padrão do print)
    else:#Se opcao não for 'i', 'a' nem 'l', cai aqui: opção inválida
        print('Por favor, escolha i, a ou l.')#Mensagem avisando para o usuário escolher uma das opções válidas.









