'''
pessoa = {
    'nome' : 'Erasmo Carlos',
    'sobrenome' : 'Tremendao',
    'idade' : '69',
    'altura' : 1.7,
    'enderecos': [
        {'rua': 'santosvila', 'numero': 121},
        {'rua':'petropolis', 'numero': '321'},
    ] ,
        
    
}

print(pessoa['nome'])

for chave in pessoa:
    print(chave, pessoa[chave])
'''
chave = 'nome_completo'
#nova_pessoa['nome'] = chave
nova_pessoa = {}

nova_pessoa[chave]= 'Hector Bonilla'
#permite que sobreescreva o campo assim:
nova_pessoa[chave]= 'Inigo Montoya'

print(nova_pessoa[chave])