num = int(input('Digite um número: '))

### Condição ser menor que 1 o programa não avança. ###
if num < 1:
    print('Digite um número inteiro maior que zero...')

### Laço para exibir os números ate o valor dado pelo usuario. ###
cont = 0
for x in range(1, num + 1):
    print(x, end=' ')
    if num % x == 0:
        cont = cont + 1

### Condição de exibição
# se o número tiver mais de duas divisões ele é considerado um número não primo.
# se o número tiver duas divisões possiveis ele é considerado um número primo ###

if cont == 2:
    print(f'\n\nO número {num} foi dividido {cont} vezes por isso ele é primo.')
else:
    print(f'\n\nO número {num} foi dividido {cont} vezes por isso ele não é um número primo.')