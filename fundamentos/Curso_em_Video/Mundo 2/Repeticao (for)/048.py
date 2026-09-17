soma = 0
cont = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        cont = cont + 1
        soma = soma + x
print(f'Resultado da Soma dos {cont} números múltiplos de três e que se encontram no intervalo de 1 até 500 é: {soma}.')
