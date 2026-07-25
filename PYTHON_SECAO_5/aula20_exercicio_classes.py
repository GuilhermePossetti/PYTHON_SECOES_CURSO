""" Exercicio com classes
1 Crie uma classe Carro (Nome)
2 Crie uma classe Motor (Nome)
3 Crie uma classe Fabricante (Nome)
4 Faça a ligação entre Carro tem Motor
OBS: Um motor pode ser de vários carros
5 faça a ligação entre Carro e Fabricante
OBS: Um fabricante pode fabricar vários carros
Exiba o nome do carro, motor e fabricante na tela """

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property #serve para transformar um método em “atributo” acessível.
    def motor(self):
        return self._motor
    
    @motor.setter #Ele serve para definir (atribuir) um valor a um atributo controlado pelo @property
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome

saveiro = Carro ('Saveiro') 
cvt_1_ponto_6 = Motor ('CVT, 1.6cv')
volksvagen = Fabricante ('Volksvagen')

saveiro.fabricante = volksvagen
saveiro.motor = cvt_1_ponto_6
print(saveiro.nome, saveiro.fabricante.nome, saveiro.motor.nome)



