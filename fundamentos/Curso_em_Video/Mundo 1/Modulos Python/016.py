# O programa lé um valor real qualquer pelo teclado e mostra na tela a sua porção Inteira.
import math
num = float(input('Digite um número: '))
num_plus = math.trunc(num)
print('O número digitado foi {} em real, em inteiro ele fica: {}'.format(num,num_plus))