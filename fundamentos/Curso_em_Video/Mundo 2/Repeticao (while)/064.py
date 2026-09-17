num = int(input('Digite Um valor [999 para parar]: '))
soma = 0
cont = 0

while num != 999:
    soma = soma + num
    num = int(input('Digite Um valor [999 para parar]: '))
    cont += 1

print(f'Você digitou {cont} números a soma é igual a {soma}')