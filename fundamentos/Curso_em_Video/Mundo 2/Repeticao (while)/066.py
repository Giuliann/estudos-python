cont = 0
soma = 0
while True:
    num = int(input('Digite um valor ou digite [999] para parar: '))
    cont += 1
    if num == 999:
        break
    soma += num

print('Programa finalizado')
print(f'Você digitou {cont} números a soma deles é {soma}')