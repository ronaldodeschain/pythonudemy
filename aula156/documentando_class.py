"""Documentando Classes

Este é um exemplo de documentação de classes
"""

class Foo:
    """este é um exemplo de descrição de clase
    
    aqui um texto descritivo 
    para, descrever redundantemente o codigo
    """
    def soma(self,x:int | float ,y: int | float) -> int|float:
        """
        Soma x e y

        :param x: Numero 1
        :type x: int or float
        :param y: Numero 2
        :type y: int or float

        :return: A soma entre x e y
        :rtype: int or float
        """