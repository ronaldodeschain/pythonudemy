#Exercicio - Unir Listas
#Criar uma função Zipper 
#o trabalho da funcao é unir duas listas em ordem
# use todos os valores da menor lista
#Ex:
# ['Salvador','Ubatuba', 'Belo Horizonte']
# ['BA','SP','MG','RJ']
#Resultado
#[('Salvador','BA'),('Ubatuba', 'SP'),('Belo Horizonte', 'MG')]

def zipper(l1,l2):
    intervalo = min(len(l1),len(l2))
    print(min(1,2))
    return [
        (l1[i],l2[i]) for i in range(intervalo)
    ]
from itertools import zip_longest


l1 = ['Salvador','Ubatuba', 'Belo Horizonte']
l2 = ['BA','SP','MG','RJ']
print(zipper(l1,l2))
print('exemplos de zip')
print(list(zip(l1,l2)))
print(list(zip_longest(l1,l2,fillvalue='Carapicuira')))