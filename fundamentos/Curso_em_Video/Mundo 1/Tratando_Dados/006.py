# Esse Programa recebe um número inteiro e exibe seu dobro, seu triplo e sua raiz quadrada.
num = int(input(' Digite um valor: '))
print(' '*20)
print(' O dobro de {} é: {}\n e seu triplo é: {}\n e sua raiz quadrada é: {:.0f}'.format(num, num * 2, num * 3, num**(1/2)))
print(' '*20)
