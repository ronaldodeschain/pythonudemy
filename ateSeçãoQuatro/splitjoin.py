frase = 'olha isso, aqui ta muito bom'
lista_palavras = frase.split(', ')

lista_palavras_fixed = []
for i,frase in enumerate(lista_palavras):
    lista_palavras_fixed.append(lista_palavras[i].strip())

#print(lista_palavras)
#print(lista_palavras_fixed)

frases_unidas = '-'.join(lista_palavras_fixed)
print(frases_unidas)


