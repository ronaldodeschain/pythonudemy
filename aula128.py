# Métodos de classe + factories (fábricas)
# São metodos onde 'self' será 'cls', ou seja, 
# ao invés de receber a instacia no primeiro 
# parametro, recebemos a propria classe.

class Pessoa:
    ano = 2023 #atributo de classe

    def __init__(self,nome,idade):
        self.nome = nome 
        self.idade = idade 

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls,nome):
        return cls(nome,50)
    
p1 = Pessoa('Joao',34)
p2 = Pessoa.criar_com_50_anos('Joajinha')
print(Pessoa.ano)
Pessoa.metodo_de_classe()
print(p2.nome,p2.idade)
print(f'{p2.nome} tem {p2.idade} anos')