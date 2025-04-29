# # class - Classes são moldes para criar novos objetos.
# As classes geram novos objetos (instancias) que 
# podem ter seus proprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados 
# internos para realizar varias ações. 
# Por convenção, usamos Pascalcase para nomes de classes.

class Pessoa:
    def __init__(self,nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Elvis','Costelo')
# p1.nome = 'Erasmo'
# p1.sobrenome = 'Carlos'
print(p1.nome)
print (p1.sobrenome)