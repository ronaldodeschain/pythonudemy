""""Este é um módulo de exemplo

Este módulo contém funções e exemplos de 
documentação de funções.
A função soma voce já conhece ne?
"""
variavel_1 = 1

def soma(x:int | float ,y: int | float) -> int|float:
    """
    Soma x e y

    :param x: Numero 1
    :type x: int or float
    :param y: Numero 2
    :type y: int or float

    :return: A soma entre x e y
    :rtype: int or float
    """
    return x + y 