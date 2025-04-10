#746.824.890-70
"""
colete a soma dos 9 primeiros dígitos
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex: 746.824.890-79
 10 9 8 7 6 5 4 3 2 
 7  4 6 8 2 4 8 9 0 
 70 36 48 56 12 20 32 27 0

 somar todos os resultados: 301
 Multiplicar o resultado anterior por 10
 301 * 10 = 3010
 Obter o resto da divisão da conta anterior por 11
 3010 % 11 = 7
 Se o resultado anterior for maior que 9:
 resultado deve ser 0
 contrario disso:
 resultado é o valor da conta

 O primeiro digito do cpf é 7

"""

cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo = 10
total = 0
for digito in nove_digitos:
   # print(digito,contador_regressivo)
    resultado = (int(digito) * contador_regressivo)
    #print(resultado)
    total += resultado
   # print(f'o total é {total}')
    contador_regressivo -= 1

soma = total * 10
primeiro_digito = soma %11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
print(primeiro_digito)