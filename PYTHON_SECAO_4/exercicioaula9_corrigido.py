perguntas = [
    {'Pergunta' : 'Quanto é 2+2',
     'Opções' : ['1', '2', '3', '4', '5'], #dicionário
     'Resposta' : '4',},

    {'Pergunta' : 'Quanto é 5*5',
     'Opções' : ['1', '2', '25', '4', '5'], #dicionário
     'Resposta' : '25',},

    {'Pergunta' : 'Quanto é 10/2',
     'Opções' : ['1', '2', '3', '4', '5'], #dicionário
     'Resposta' : '5',},
]

qtd_acertos = 0  #guarda a quantas perguntas acertou, começa em zero
for pergunta in perguntas: #cria um laço de repetição // pergunta recebe cada dic // in perguntas percorre a lista 
    print('Pergunta:', pergunta['Pergunta'])#Pergunta aparece na tela // pergunta['Pergunta'] chama o dic que vai aparecer 'Quanto é 2+2'
    print()

    opcoes = pergunta['Opções'] #cria veriavel opções, guarda a lista de opções da pergunta atual
    for i, opcao in enumerate(opcoes): #enumerate devolve // i é o indice // opcao valor da lista // serve para numerar as opções
        print(f'{i})', opcao)# (0)=1, (1)=2, (2)=3
    print()

    escolha = input('Escolha uma opção: ')#ede algo ao usuário Tudo que entra aqui é string

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)#quantidade de itens da lista

    if escolha.isdigit():#verifica se só tem números
        escolha_int = int(escolha)#Converte string → número inteiro

    if escolha_int is not None:#Confirma que a conversão deu certo
        if escolha_int >= 0 and escolha_int < qtd_opcoes:#Garante que o número existe nas opções Evita erro de índice
            if opcoes[escolha_int] == pergunta['Resposta']:#opção escolhida Compara com a resposta correta
                acertou = True#Marca que o usuário acertou

    print()
    if acertou:
        qtd_acertos += 1#Soma 1 no contador
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')