nome = input('digite seu nome? ')
idade = input('qual sua idade? ')
if nome and idade:
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é{nome[::-1]}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')
else:
   print('Desculpe, voce deixou campos vazios.')