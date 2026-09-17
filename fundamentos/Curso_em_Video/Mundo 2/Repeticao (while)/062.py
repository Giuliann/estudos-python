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

### NOVO TERMO ###
while novo_termo != 0:
    print('\n\nQuer mostrar mais alguns termos?')
    novo_termo = int(input('Digite quantos termos quer mostrar: '))
    cont = 1

    if novo_termo > 0:
        while cont <= novo_termo:
            print(f'{termo_atual}', end='')
            print(' -> ' if cont <= total_termo else '', end='')
            termo_atual = termo_atual + rza
            cont = cont + 1
            print('PAUSA' if cont > novo_termo else '', end='')
            contador_termos = contador_termos + 1


print(f'\n\nPrograma Finalizado com o total de {contador_termos} termos')