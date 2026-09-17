# O programa recebe o valor da velocidade de um veiculo em Kmh, se o valor passar de 80kmh
veloc = int(input('Digite a velocidade do veiculo: '))
multa = 80
valorM = 7

if veloc > multa:
    print(f'Você foi multado em {(veloc - multa) * valorM}R$')
else:
    print('Você não foi multado')