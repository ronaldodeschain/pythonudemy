#groupby - agrupando valores (itertools)

from itertools import groupby

alunos = [
    {'nome':'Luiz','nota':'A'},
    {'nome':'Leticia','nota':'B'},
    {'nome':'Fabricio','nota':'A'},
    {'nome':'Rosemary','nota':'C'},
    {'nome':'Joana','nota':'D'},
    {'nome':'João','nota':'A'},
    {'nome':'Eduardo','nota':'B'},
    {'nome':'André','nota':'A'},
    {'nome':'Anderson','nota':'C'}
]

def ordena(aluno):
    return aluno['nota']

#lambda pra selecionar o parametro do sort
alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave,grupo in grupos:
    print(chave)
    print(list(grupo))



