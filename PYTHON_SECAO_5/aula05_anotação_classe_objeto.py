"""
CLASSE = fábrica / molde / projeto
OBJETO = carro já pronto

ENCAPSULAMENTO = esconder a parte interna e deixar só o que precisa ser usado. 
usar por fora, sem mexer no mecanismo por dentro.

ABSTRAÇÃO = pegar só o que importa naquele momento e ignorar o resto. 
focar no essencial e ignorar o resto.

HERANÇA = quando uma classe pega características e comportamentos de outra.
aproveitar o que já existe e acrescentar o que é específico.

POLIMORFISMO = vários veículos fazem a mesma ação de maneiras diferentes
a mesma ação, comportamentos diferentes.

Classe:
A classe é o projeto da fábrica.
Ela define coisas como:
                        todo veículo tem marca
                        todo veículo tem cor
                        todo veículo pode ligar
Ainda não existe nenhum carro real.
Só a ideia, o molde.


Objeto:
O objeto é o carro já pronto, que saiu da fábrica.
Exemplo:
          um Gol prata
          um Uno branco
          um Civic preto
Todos vieram do mesmo molde, mas são objetos diferentes.


Abstração:
Quando alguém fala carro, você já entende o principal:
- anda
- tem volante
- freio
- motor
Você não pensa imediatamente em:
                                 parafuso
                                 bomba de combustível
                                 pressão do óleo
Isso é abstração.
Você olha só o que importa naquele momento.


Encapsulamento:
Quando você entra no carro, você usa:
                                       volante
                                       freio
                                       acelerador

Mas você não precisa abrir o motor e controlar as peças uma por uma.
O funcionamento interno fica “fechado”.
Isso é encapsulamento.
Você usa por fora sem mexer no mecanismo por dentro.


Herança:
Agora pensa que existe uma classe geral chamada Veículo.
Ela define coisas que todo veículo tem.
Aí existe a classe Carro.
Carro aproveita tudo que já existe em veículo e acrescenta o que é dele.
Exemplo:
           Todo veículo pode ligar.
           Mas carro pode ter também:
           porta-malas 
           ar-condicionado
Então:
carro herda de veículo.


Polimorfismo:
Agora pensa em três objetos:
                              carro
                              moto
                              caminhão
Todos podem receber a mesma ação:
                                  ligar
Mas cada um reage de um jeito.
o carro liga de um jeito
a moto de outro
o caminhão de outro
A ação é a mesma.
O comportamento muda.
Isso é polimorfismo.


✅✅✅✅✅✅✅✅✅✅
Setter
Quando faz:
p1.nome = 'Gui'
o Python chama:
@nome.setter

Getter
Quando faz:
print(p1.nome)
o Python chama:
@property

Getter/setter:
mexem em atributos/dados

✅✅✅✅✅✅✅✅✅✅
"""





















