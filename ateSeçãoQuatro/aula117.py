import json


# pessoa = {
#     'nome':'Elvis',
#     'sobrenome':'Costelo',
#     'enderecos':[
#         {'rua':'R1','numero':32},
#         {'rua':'R2','numero':55},
#     ],
#     'altura':1.8,
#     'numeros_preferidos': (2,4,6,8,19),
#     'dev': True,
#     'nada': None,
# }

# with open('aula117.json', 'w', encoding='utf8') as arquivo:
#     json.dump(pessoa,arquivo,indent=2)

#aqui podemos abrir o arquivo json que criei acima
with open('aula117.json','r',encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])