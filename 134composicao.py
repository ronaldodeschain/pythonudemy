# class Escritor:
#     def __init__(self,nome)-> None:
#         self.nome = nome
#         self._ferramenta = None

#     @property
#     def ferramenta(self):
#         return self._ferramenta
    
#     @ferramenta.setter
#     def ferramenta(self,ferramenta):
#         self._ferramenta = ferramenta

# class FerramentaDeEscrever:
#     def __init__(self,nome):
#         self.nome = nome
    
#     def escrever(self):
#         return f'{self.nome} está escrevendo'
    

# escritor = Escritor('Olavo Bilac')
# pena = FerramentaDeEscrever('Pena de pato')
# caneta = FerramentaDeEscrever('Caneta')
# escritor.ferramenta = pena
# escritor.ferramenta = caneta

# print(pena.escrever())
# print(caneta.escrever())
# print(escritor.ferramenta.escrever())

#Agregação e composição
