from datetime import datetime
data_atual = datetime.today().year
h_mais_velho = ''
idd_mais_velho = 0
media = 0
soma = 0
total_mulhres20 = 0

for x in range(1, 5):
    print('=' * 3, x, 'Pessoa', '=' * 3)
    nome = input('Nome: ')
    data_user = int(input('ano de nascimento: '))
    sexo = str(input('Sexo [M] ou [F]: ').upper())
    idade = data_atual = data_user
    soma = soma + idade
    if x == 1 and sexo == 'M':
        idd_mais_velho = idade
        h_mais_velho = nome
    if sexo == 'M' and idade > idd_mais_velho: 
        idd_mais_velho = idade
        h_mais_velho = nome
    if sexo == 'F' and idade < 20:
        total_mulhres20 = total_mulhres20 + 1

media = soma / 4
print(f'O total de mulheres com menos de 20 anos é {total_mulhres20}')
print(f'Idade do homem mais velho é: {idd_mais_velho} e seu nome é: {h_mais_velho}')
print(f'A idade media do grupo é: {media:.0f}')