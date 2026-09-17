cont_homens = 0
cont_mulher_20 = 0
cont = 0
print('     CADASTRO')
print('=' * 20) 
idd = int(input('Digite sua idade: '))
sexo = input('Diga seu sexo [F/M]: ').upper()
while True:
    select = input('Gostaria de se cadastra [S/N]: ').upper()
    if select == 'N':
        break
    idd = int(input('Digite sua idade: '))
    if idd > 18:
        cont += 1
    sexo = input('Diga seu sexo [F/M]: ').upper()
    if sexo == 'M':
        cont_homens += 1
    elif sexo == 'F' and idd >= 20:
        cont_mulher_20 += 1



print(f'Tem um total de {cont} pessoas maiores de 18 anos')
print(f'O total de homens cadastrados é {cont_homens}')
print(f'O total de mulheres com menos de 20 anos é {cont_mulher_20}')