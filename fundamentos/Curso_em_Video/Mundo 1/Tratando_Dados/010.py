# O programa lé o valor em reais do usuario e converte em dólares.
real = float(input('Digite um valor em Reais: '))
usd = (real / 5.43)
print('O valor digitado foi: {:.2f}R$ e seu valor em dólares é: {:.2f}' .format(real, usd))