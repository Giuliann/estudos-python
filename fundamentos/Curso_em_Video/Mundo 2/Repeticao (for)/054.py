from datetime import datetime
ano_atual = datetime.today().year 
cont_maior = 0
cont_menor = 0
for x in range(1, 8):
    nasci = int(input(f'Em que ano a {x}° nasceu: '))
    if ano_atual - nasci >= 18:
        cont_maior = cont_maior + 1
    elif ano_atual - nasci < 18:
        cont_menor = cont_menor + 1
print(f'\nO total de pessoas maiores de idade é {cont_maior}')
print(f'e o total que ainda não são de maior é {cont_menor}')