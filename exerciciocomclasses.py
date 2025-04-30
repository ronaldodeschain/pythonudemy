#Exercicio com classes
#1 - Crie uma classe Carro (nome)
#2 - Crie uma classe Motor (nome)
#3 - Crie uma classe fabricante (nome)
#4 - Faça a ligacao entre Carro e motor
#Obs: um motor pode ser de varios carros
#5 - Faca a ligacao entre carro e fabricante
#Obs: um fabriante pode fabricar varios carros
#Exiba o nome do carro, motor e fabricante na tela
class Carro:
    def __init__(self,nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self,valor):
        self._motor = valor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self,valor):
        self._fabricante = valor

class Motor:
    def __init__(self,nome):
        self.nome = nome

class Fabricante:
    def __init__(self,nome):
        self.nome = nome

fusca = Carro('Fusca')
vw = Fabricante('Volks')
v8 = Motor('V8')
fusca.fabricante = vw
fusca.motor = v8
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)