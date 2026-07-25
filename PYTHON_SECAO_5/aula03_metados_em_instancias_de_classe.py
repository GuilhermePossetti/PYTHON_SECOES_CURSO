# Métados em instâncias de Classes Python
# classes são moldes que geram novas instancias, objeto

class  Carro:
    def __init__(self, nome): #self instancia da classe
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome= 'celta')
print(celta.nome)
celta.acelerar()
        