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