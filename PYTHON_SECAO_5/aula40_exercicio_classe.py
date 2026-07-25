"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A idéia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas correntes tem um limete extra

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        cliente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta


Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguintes maneneira:

    Banco tem cintas e clientes (Agregação)
    * chegar se a agência é daquele banco
    * checar se o cliente é daquele banco
    * checar se a conta é daquele banco

Só será possivel sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método
"""