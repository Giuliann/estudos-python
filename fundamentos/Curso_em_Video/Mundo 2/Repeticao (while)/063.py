termos = int(input('Quantos termos você quer mostrar: '))
cont = 0
t1 = 0
t2 = 1

while cont < termos:

    print(f'{t1} ', end='-> ')
    proximo_termo = t1 + t2
    t1 = t2
    t2 = proximo_termo
    cont += 1

print('Fim')