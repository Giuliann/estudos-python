# O programa 'pensa' em um número aleatorio, recebe um valor do usaurio e diz se os valores são iguais.
import random

print('--' *11)
print('---Jogo de Adivinha---')
print('--' *11)
print('Estou pensando... em um número entre 0 a 5')
print('Você consegue adivinhar?')

resp = int(input('\nDigite um Número de 0 a 5: '))
num = random.randint(0, 5)


if resp == num:
    print(f'O número que eu pensei foi {num}')
    print('!!! Parabéns você acertou !!!')
elif resp > 5:
    print('Você digitou um número maior que 5')
elif resp < 0:
    print('Você digitou um número menor que 0')
else:
    print(f'O número que eu pensei foi {num}')
    print('-- Você errou --')
    print('Tente Novamente...')
