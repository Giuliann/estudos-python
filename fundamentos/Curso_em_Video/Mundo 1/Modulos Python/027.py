# O programa que lé o nome completo de uma pessoa, mostra em seguida o primeiro e o último nome separadamente.
nome = input('Digite seu Nome: ').strip().split(' ')
print(f'O seu primeiro nome é {nome[0]} e a ultima parte do seu nome é {nome[-1]}')