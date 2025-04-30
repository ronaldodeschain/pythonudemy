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
# class Carrinho:
#     def __init__(self):
#         self._produtos = []

#     def total(self):
#         return sum([p.preco for p in self._produtos])
    
#     def inserir_produtos(self,*produtos):
#         # for produto in produtos:
#         #     self._produtos.append(produto)
#         #self._produtos.extend(produtos)
#         self._produtos += produtos

#     def listar_produtos(self):
#         print()
#         for produto in self._produtos:
#             print(f'Nome: {produto.nome} - preco: {produto.preco}')
#         print()

# class Produto:
#     def __init__(self,nome,preco):
#         self.nome = nome
#         self.preco = preco

# carrinho = Carrinho()
# p1,p2 = Produto('Caneta',1.20),Produto('Camiseta',20)
# carrinho.inserir_produtos(p1,p2)
# carrinho.listar_produtos()
# print(carrinho.total())

#Composição
# class Cliente:
#     def __init__(self,nome):
#         self.nome = nome
#         self.enderecos = []

#     def inserir_endereco(self,rua,numero):
#         self.enderecos.append(Endereco(rua,numero))

#     def lista_endereco(self):
#         for endereco in self.enderecos:
#             print(endereco.rua,endereco.numero)

# class Endereco:
#     def __init__(self,rua,numero):
#         self.rua = rua
#         self.numero = numero

# cliente1 = Cliente('Maria')
# cliente1.inserir_endereco('Suas', 1513)
# cliente1.inserir_endereco('blaeas',54534)

# # print(cliente1.enderecos[0].rua)
# # print(cliente1.enderecos[1].rua)
# cliente1.lista_endereco()

# print('Fim do codigo')