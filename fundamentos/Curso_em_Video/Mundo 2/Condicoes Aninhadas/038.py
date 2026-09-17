# O programa recebe dois valores e exiber qual deles é o maior, ou se os dois são iguais.
print('Digite dois números')
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

if num1 > num2:
    print('O número {} é maior que {}' .format(num1, num2))
elif num2 > num1:
    print('O número {} é maior que {}' .format(num2, num1))
elif num1 == num2:
    print('O número {} e {} são iguais' .format(num1, num2))