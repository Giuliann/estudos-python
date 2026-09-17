frase = str(input('Digite uma frase: ')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
inverso = ''

for x in range(len(junto) - 1, -1, -1):
    inverso += junto[x]

print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print(f'A frase: {junto} é um palindromo')
else:
    print(f'A frase: {junto} não é um palindromo')