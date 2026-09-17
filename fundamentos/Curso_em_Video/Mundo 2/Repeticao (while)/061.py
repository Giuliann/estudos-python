# O programa exibe os 10 primeiros termos de uma PA e pergunta ao usuario se ele quer exibir mais algumas.
print('=' * 5, 'Progressão Aritmética' ,'=' * 5)
num = int(input('Digite o primeiro termo: '))
rza = int(input('Digite a razão: '))
termo_atual = num
total_termo = 10
novo_termo = 1
contador_termos = total_termo
cont = 1


### 10 PRIMEIROS TERMOS ###
while cont <= total_termo:
    print(f'{termo_atual}', end='')
    print(' -> ' if cont <= total_termo else '', end='')
    termo_atual = termo_atual + rza
    cont = cont + 1
    print('PAUSA' if cont > total_termo else '', end='')
