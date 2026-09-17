soma = 0
cont = 0
for x in range(1, 7):
   val = int(input(f'Digite o {x}° valor: '))
   if val % 2 == 0:
        soma = soma + val
        cont = cont + 1
print(f'A soma dos {cont} números pares é: {soma}')