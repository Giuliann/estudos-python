# O programa recebe um número inteiro e informa ao usuario se o número é par ou impar

num = int(input('Digite um número: '))
result = num % 2

if result == 0:
    print(f'O número {num} é par')
else:
    print(f'O número {num} é impar')