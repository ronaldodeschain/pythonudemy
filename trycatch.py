#Try, Except, Else e Finally

#a = 18
#b = 0
#c = a / b
'''
try:
    a = 18
    b = 0
    print(b[0])
    print('linha 1'[1000])
    c = a / b 
    print('linha 2')
except ZeroDivisionError:
    print('divisao por zero.')
except NameError:
    print('Nome b nao esta definido')
except (TypeError,IndexError) as error:
    print('Type error + IndexError')
    print('MSG: ', error)
    #como identificar o tipo de erro
    print('Nome: ',error.__class__.__name__)

#  quando cai aqui tem como tentar localizar
#  o ponto do erro para identificar o seu tipo para 
#  melhorar o corido
except Exception:
    print('Erro desconhecido')

print('Continuar')

'''

'''
/////
try:
   print('abrir arquivo')
   8/0
except Exception as e:
   print(e.__class__.__name__)

finally:
   print('fechar arquivo')
   ///
   '''

