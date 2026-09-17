import random
print('=' * 5, 'Lista de Opções', '=' * 5)
print('(1) Pedra')
print('(2) Papel')
print('(3) Tesoura')
user = int(input())
comp = random.randint(1, 3)
if user <= 0 or user >= 4:
    print('Por favor digite uma Opção valida')
    exit()
### Computador Escolhe Pedra ###
if comp == 1:
    print('Computador escolheu Pedra')
    if user == 1:
        print('EMPATE')
    elif user == 2:
        print('Parabéns Você Ganhou!!!')
    elif user == 3:
        print('Você Perdeu, Tente Novamente...')

### Computador Escolhe Tesoura ###
elif comp == 2:
    print('Computador escolheu papel')
    if user == 1:
        print('Você Perdeu, Tente Novamente...')
    elif user == 2:
        print('EMPATE')
    elif user == 3:
        print('Parabéns Você Ganhou!!!')

### COmputador Escolhe Papel ###
elif comp == 3:
    print('Computador escolheu Tesoura')
    if user == 1:
        print('Parabéns Você Ganhou!!!')
    elif user == 2:
        print('Você perdeu, Tente Novamente...')
    elif user == 3:
        print('EMPATE')
