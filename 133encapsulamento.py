#Python não tem modificadores de acesso
# _ (um underline) = protected
#   nao deve ser usado fora da classe
# __(dois underlines) = private só para a classe em que foi definido
# `name mangling` (desconfiguraçao de nomes)
class Foo:
    def __init__(self):
        self.public = 'Isso é publico'
        self._protected = 'Isso é protegido'
        self.__private = 'Isso é privado'
        self._metodo_protected()

    def metodo_publico(self):
        #self._metodo_protected()
        #print(self._protected)
        print(self.__private)
        return 'metodo_publico'
    
    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'
    
    def __metodo_private(self):
        print('_metodo_private')
        return '__metodo_private'


f = Foo()
#NÃO FAZER - Nao existe o parametro mas uma
#  convenção para nao usar assim
#print(f._protected)
f.metodo_publico()
#print(f.__metodo_private())
#Did you mean: '_Foo__metodo_private'?
# nao faz isso === print(f._Foo__metodo_private())