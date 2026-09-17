valor = int(input('Qual o valor a ser sacado: R$ '))
total = valor
ced = 50
total_cedula = 0
while True:
    if total >= ced:
        total -= ced
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de cedulas de {ced} foi de {total_cedula}')
        if ced == 50:
            ced = 20
            total_cedula = 0
        elif ced == 20:
            ced = 10
            total_cedula = 0
        elif ced == 10:
            ced = 1
            total_cedula = 0
        if total == 0:
            break



