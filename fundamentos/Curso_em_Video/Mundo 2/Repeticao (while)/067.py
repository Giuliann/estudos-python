while True:
    print('=' * 20)
    num = int(input('Qual Tabuada você quer ver? '))
    print('=' * 20)
    cont = 0
    if num < 0:
        break
    while True:
        cont += 1
        tabuada = num * cont
        if cont <= 10:
            print(f'{num} x {cont} = {tabuada}')
        elif cont > 10:
            break

print('Fim do programa...')
