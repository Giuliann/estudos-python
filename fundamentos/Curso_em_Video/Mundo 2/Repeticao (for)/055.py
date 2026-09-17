# O programa lé o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for x in range(1, 6):
    peso = int(input(f'Qual o peso da {x}° pessoa: '))
    if x == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'\nO maior peso é: {maior}Kg')
print(f'E o menor peso é: {menor}Kg')
