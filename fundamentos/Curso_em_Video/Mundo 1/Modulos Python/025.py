# O programa lé o nome de uma pessoa e diz se ela tem “SILVA” no nome.
nome = input('Digite seu nome: ').upper().strip()

result = 'SILVA' in nome

if result == True:
    print('Seu nome tem Silva')
else:
    print('Seu nome não tem Silva')
