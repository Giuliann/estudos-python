# O programa lé o nome completo de uma pessoa e exibe:
# - Seu nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ').strip()

print(f'\nSeu nome todo em maiúsculo: {str.upper(nome)}')
print(f'\nSeu nome todo em maiúsculo: {str.lower(nome)}')

print(f'\nO número de letras do seu nome: {len(nome)-nome.count(' ')}')

print(f'\nO número de letras do seu primeiro nome: {nome.find(' ')}')