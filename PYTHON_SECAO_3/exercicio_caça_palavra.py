"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

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
