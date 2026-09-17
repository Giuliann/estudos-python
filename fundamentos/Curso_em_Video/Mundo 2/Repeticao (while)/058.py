# Versão 2.0 do jogo do DESAFIO 28 onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantas tentativas foram necessários para vencer.
import random
print('='*5, 'JOGO ADVINHA 2.0', '='*5 )
palpite_comp = random.randint(0, 10)
palpite_user = int(input('Digite o seu palpite: '))
cont = 1

while palpite_user != palpite_comp:
    print(f'Comp {palpite_comp} // User {palpite_user}')
    palpite_comp = random.randint(0, 10)
    print('Você errou, tente novamente')
    palpite_user = int(input('Digite o seu palpite: '))
    cont += 1
    print('\n')


print(f'Comp {palpite_comp} // User {palpite_user}')
print('Parabéns você acertou')
print(f'O número de tentativas foi: {cont}')