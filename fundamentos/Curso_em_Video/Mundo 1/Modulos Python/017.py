# O programa lé o valor do cateto oposto e do cateto adjacente de um triângulo retângulo, calcula e exibe o comprimento da hipotenusa.
import math
catadj = float(input('Digite o valor do cateto adjacente do triângulo: '))
catops = float(input('Digite o valor do cateto oposto do triângulo: '))
hipo = math.hypot(catadj, catops)
print('O valor da hipotenusa é: {:.2f}'.format(hipo))