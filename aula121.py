# Métodos em instancias de classe Python

class Carro:
    def __init__(self,nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fuca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()
Carro.acelerar(fusca)