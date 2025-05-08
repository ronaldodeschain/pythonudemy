def adiciona_repr(class_):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    class_.__repr__=meu_repr
    return class_

def meu_planeta(metodo):
    def interno(self,*args,**kwargs):
        resultado = metodo(self,*args,**kwargs)
        
        if 'Terra' in resultado:
            return 'Voce está em casa'
        return resultado
    return interno


class MyReprMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr


#sintaxsugar 
@adiciona_repr
class Time():
    def __init__(self, nome):
        self.nome = nome

    
@adiciona_repr
class Planeta():
    def __init__(self,nome):
        self.nome = nome

    
    @meu_planeta
    def falar_nome(self):
        return f'O planeta é {self.nome}'

#agora eu posso chamar o metodo repr para 
# adicionar ele as classes que eu quiser
# Time = adiciona_repr(Time)
brasil = Time('Brasil')
portugal = Time('Guiana Brasileira')
terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)
print(terra)
print(marte)

print(terra.falar_nome())
print(marte.falar_nome())
