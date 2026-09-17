# O programa recebe um valor e converte para as bases: binaria, octal ou hexadecimal.
num = int(input('Digite um número: '))
print('Qual a base númerica você quer transformar o seu número: ')
print('(1) Binario')
print('(2) Octal')
print('(3) Hexadecimal')

select = int(input(''))
if select == 1:
    print('O número {} em binario é {}' .format(num, bin(num)[2:]))
elif select == 2:
    print('O número {} em octal é {}' .format(num, oct(num)[2:]))
elif select == 3:
    print('O número {} em Hexadecimal é {}' .format(num, hex(num)[2:]))
else:
    print('Escolha uma das opções listadas...')
