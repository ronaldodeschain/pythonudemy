#list comprehension em Python
#list comprehension é uma forma rapida de criar listas
#a partir de iteraveis
import pprint
def p(v):
    pprint.pprint(v,sort_dicts=False,width=40)
#print(list(range(10)))
'''
lista = []
for numero in range(10):
    lista.append(numero)
#print(lista)
lista = [
    numero * 2
    for numero in range(10)]
print(lista)
'''
#Mapeamento de dados em list comprehension
produtos = [
    {'nome':'p1','preco':20},
    {'nome':'p2','preco':10},
    {'nome':'p3','preco':30},
]
novos_produtos = [
    #assim eu consigo alterar o preco 
    # #tabelado de todos os produtos aumtomaticamente.
   {**produto,'preco':produto['preco']*1.05}
   if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
#print(novos_produtos)
#print(novos_produtos)
#p(novos_produtos)
#filtro
#lista = [n for n in range(10)if n < 5]
novos_produtos = [
   {**produto,'preco':produto['preco']*1.05}
   if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10
]
p(novos_produtos)

