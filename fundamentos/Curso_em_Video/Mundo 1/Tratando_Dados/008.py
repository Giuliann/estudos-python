# O programa lé um valor dado em metros e o converte em centimetros e em milimetros.
num = int(input('Digite um valor em metros: '))
print('O valor digitado foi: {}m'.format(num))
print('O valor de {}m em metros equivale a {}cm em centimetros e equivale a {}mm em milimetros'.format(num,num * 100, num * 1000))