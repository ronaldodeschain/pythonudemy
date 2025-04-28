import os

caminho_arquivo = 'C:\\Users\\Usuario\\Documents\\python\\pasta\\'
caminho_arquivo += 'aula116.txt'

#ctrl +  k +c / ctrl + k + u
# arquivo = open(caminho_arquivo, 'w') 
# #sempre fechar depois
# arquivo.close() 

#com with open
# with open(caminho_arquivo, 'w+') as arquivo:
#      arquivo.write('Linha 1\n')
#      arquivo.write('Linha 2\n')
#      arquivo.writelines(
#           ('Linha 3\n','Linha 4\n')
#      )
#      arquivo.seek(0, 0)
#      print(arquivo.read())

# print('#' * 10)

# with open(caminho_arquivo, 'r') as arquivo:
#      print(arquivo.read())
#      print('Lendo\n')
#      arquivo.seek(0,0)
#      print(arquivo.readline(), end='')
#      print(arquivo.readline().strip())
#      print(arquivo.readline().strip())

#      print('READLINES')
#      arquivo.seek(0,0)
#      for linha in arquivo.readlines():
#           print(linha.strip())

#append mode escrever a partir do fim do arquivo
#encoding garante o idioma e o uso dos caracteres especiais
with open(caminho_arquivo, 'a+', encoding='utf8') as arquivo:
     arquivo.write('Linha 1\n')
     arquivo.write('Linha 2\n')
     arquivo.writelines(
          ('Linha 3\n','Linha 4\n')
     )
     arquivo.seek(0,0)
     for linha in arquivo.readlines():
          print(linha.strip())

#os.remove(caminho_arquivo)
#os.rename(caminho_arquivo,'aula116-2.txt')