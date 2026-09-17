# O programa que lé um número qualquer e mostra o seu fatorial.
from math import factorial
num = int(input('Digite um valor: '))
fac = factorial(num)
cont = num
fatorial = 0
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    cont = cont - 1
print(fac, end='')

