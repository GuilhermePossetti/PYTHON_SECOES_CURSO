"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
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