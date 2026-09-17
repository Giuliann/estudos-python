# O programa lé um número de 0 a 9999 e mostra na tela cada um dos dígitos separados.

frase = int(input('Digite um número: '))

print(f'Analisando o número {frase}')
print(f'Milhar: {frase // 1000 % 10 :.0f}')
print(f'Centena: {frase // 100 % 10 :.0f}')
print(f'Dezena: {frase // 10 % 10 :.0f}')
print(f'Unidade: {frase // 1 % 10 :.0f}')
