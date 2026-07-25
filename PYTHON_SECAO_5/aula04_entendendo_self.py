# Classe - Molde (sem dados)
# Instânias da classe (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias
# Na classe o self é a própria instãncia

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome = 'Celta')
print(celta.nome)
celta.acelerar()


############ EXERCÍCIO ###############

class Cachorro:
    def __init__(self, nome):
        self.nome = nome

    def latir(self):
        print(f'{self.nome} está latindo')

cachorro = Cachorro('Sai cachorro')
print(cachorro.nome)
cachorro.latir()