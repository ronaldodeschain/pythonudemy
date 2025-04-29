#@property - um getter no modo Pythonico 
#getter - um metodo para obter um atributo
#modo pythonico - modo do python fazer as coisas
#@property - é uma propriedade do objeto, ela é um
#metodo que se comporta como um atributo
#geralmente é usada nas seguintes situações:
# - como getter
# - p/evitar quebrar codigo cliente
# - p/habilitar setter
# - p/executar ações ao obter um atributo
class Caneta:
    def __init__(self,cor):
        #private protected public
        self.cor = cor 
    
    def get_cor(self):
        return self.cor

caneta = Caneta('Azul')
print(caneta.cor)