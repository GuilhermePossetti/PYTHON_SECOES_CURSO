########################################################################################################
######################                     ESCOPO                                    ###################
"""o que é escopo??

conceito= é o contexto onde uma variável é definida e pode ser acessada. 
Ele determina de onde uma variável pode ser usada no código.

É tbm a região do código onde um nome está diretamento acessivel
Ele determina os limites e o tempo de vida dos nomes definidos indiretamente

Escopo é usado para encapsular o código e evitar colisões de nomes e efeitos
colaterais indesejados

O python tem quatro tipos de escopos: Built-In, Global, Enclosing e Local.
Esses escopos são dinamicos. O interpretador pode criar e apagar em tempo de execução

Cada escopo tem seu "espaço de nomes" (namespace), que é um local onde os 
nomes e seus respectivos objetos são armazenados

Escopo Built-In: é o nível mais externo de escopo, onde ficam as funções, 
tipos e constantes nativas da linguagem, disponíveis automaticamente em qualquer programa
É o escopo que contém tudo o que o Python já traz pronto, sem precisar importar nada.

Global: das variáveis declaradas fora de funções ou classes, ou seja, no corpo principal do arquivo
Essas variáveis podem ser lidas em qualquer função, mas não podem ser modificadas dentro de uma função 
sem autorização explícita. É o escopo que pertence ao arquivo (módulo) onde o código está escrito.

Enclosing: é o escopo das funções externas quando existe função dentro de função (funções aninhadas)
Ele fica entre o escopo local e o global na regra LEGB
É o escopo da função “pai”, cujas variáveis podem ser acessadas pela função interna.

Local: escopo das variáveis declaradas dentro de uma função.
Essas variáveis só existem durante a execução da função e não podem ser acessadas fora dela
Tem prioridade máxima na busca de variáveis.
"""
########################################################################################################
######################                     NAMESPACE                                 ###################
"""
O que é namespace? é um espaço onde os nomes (identificadores) são armazenados e associados a objetos
 (variáveis, funções, classes, etc.)
 cada chave é um nome que vc define e o valor é o objeto correspondente no seu código
 sempre que vc cria um nome, essa associação é guardada dentro de um namespace

 `vars()`: retorna o atributo '__dict__' de um objeto que é onde seus
           atributos são armazenado. se chamada sem argumentos, 'vars()' se
           comporta exatamente como 'locals()', retornando o namespace local

`dis()`: sem argumentos, 'dir()' lista todos os nomes disponivel no escopo
         atual. Com um objeto como argumento. tenta listar todos os nomes acessiveis nele
         (como métodos e atributos). note que di()
         retorna apenas os nomes, não os objetos ou seus valores.
"""

##################### RELAÇÃO ENTRE O ESCOPO E O NAMESPACE ##############################
""" 
São assuntos interligados e muitas vezes confundidos
mas a diferença deles é bem simples

ESCOPO: define os limites e o tempo de vida de um trecho de código que tem um namespace

NAMESPACE: é um objeto real que guarda os nomes e seus respectivos valores

É por isso que, ao fazer 'import x', dizemos que 'x' é um namespace, ele
guarda nomes como 'x.func_global()', 'x.valor', ect
"""