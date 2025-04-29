# Métodos em instancias de classe Python

# class Carro:
#     def __init__(self,nome):
#         self.nome = nome

#     def acelerar(self):
#         print(f'{self.nome} está acelerando...')

# fusca = Carro('Fuca')
# print(fusca.nome)
# fusca.acelerar()

# celta = Carro('Celta')
# print(celta.nome)
# celta.acelerar()
# Carro.acelerar(fusca)

# class Animal:
#     # nome = 'Leão'

#     def __init__(self,nome):
#         self.nome = nome

#         variavel = 'valor'
#         print(variavel)
    
#     def comendo(self,alimento):
#         return f'{self.nome} está comendo {alimento}'

# leao = Animal(nome='Leão')
# print(leao.nome)
# print(leao.comendo('jaguatirica'))

# class Camera:
#     def __init__(self,nome,filmando=False):
#         self.nome = nome
#         self.filmando = filmando

#     def filmar(self):
#         if self.filmando:
#             print(f'{self.nome} Já está filmando...')
#             return 
        
#         print(f'{self.nome} está filmando...')
#         self.filmando = True

#     def parar_filmar(self):
#         if not self.filmando:
#             print(f'{self.nome} Não está filmando...')
#             return 
        
#         print(f'{self.nome} está parando de filmar...')
#         self.filmando = False

#     def fotografar(self):
#         if self.filmando:
#             print(f'{self.nome} não pode fotografar enquanto filma')
#             return
        
#         print(f'{self.nome} está fotografando')

# c1 = Camera('Canon')
# c2 = Camera('Sony')
# c2.filmar()
# c2.filmar()
# c2.fotografar()
# c2.parar_filmar()
# c2.fotografar()
# print()
# #ctrl + D permite selecionar um campo a mais por vez
# c1.filmar()
# c1.filmar()
# c1.fotografar()
# c1.parar_filmar()
# c1.fotografar()

#Atributos de Classe
class Pessoa:
    ano_atual = 2025

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Joao',35)
p2 = Pessoa('Julia',27)

print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())