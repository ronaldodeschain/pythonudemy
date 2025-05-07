# Context Manager com classes
# Voce pode implementar seus próprios protoclos
# apenas implementando os dunder methos que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# esta interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
#Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo ele de pato
# Para criar um context manager, os métodos __enter e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e
# traceback. Se ele retornar True, exceção no with será
# suprimida.
class MyOpen:
    def __init__(self,caminho_arquivo,modo):
        print('init')
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo,self.modo,encoding='utf8')
        return self._arquivo
    
    def __exit__(self,class_exception,exception_,traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()
        
        print(class_exception)
        print(exception_)
        print(traceback_)

        return True #tratei a exceçào de alguma forma


#retorno do enter vai para a variavel arquivo
with MyOpen('aula149.txt','w') as arquivo:
    print('with',arquivo)
    arquivo.write('Linha 1\n',123)