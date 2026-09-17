# O programa calcula o preço do aluguel de um carro, com base nos dias de uso do veiculo e na quantidade de kilometros percorridos.
print('Valor do aluguel de veiculos é 60.00R$ a diaria e 0.15R$ por kilometros(km)')
dia = float(input('Quantos dias alugado: '))
km = float(input('Quantos km pecorridos: '))
val = (dia * 60) + (km * 0.15)
print('O valor do aluguel ficou {}'.format(val))
