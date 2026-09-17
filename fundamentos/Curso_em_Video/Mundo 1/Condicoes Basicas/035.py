# O programa recebe os valores de três retas e informa se juntas as retas formam um triangulo.
print('Informe o comprimento de três retas para formar um triangulo')
reta1 = float(input('primeira reta: '))
reta2 = float(input('segunda reta: '))
reta3 = float(input('terceira reta: '))


if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta3 + reta2 > reta1:
    print('É um Triangulo')
else:
    print('Não é um triangulo')