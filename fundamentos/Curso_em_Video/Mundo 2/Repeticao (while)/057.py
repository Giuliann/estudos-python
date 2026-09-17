# O programa lé o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, o programa pede para digitar novamente até ter um valor correto.

print('Usando (M) para masculino e (F) para feminino')
sexo = str(input('Digite seu sexo: ')).upper().strip()

while sexo not in 'FM':
    print('Dado não valido, por favor tente novamente...')
    print('Usando (M) para masculino e (F) para feminino')
    sexo = str(input('Digite seu sexo: ')).upper().strip()

print('fim')
print(f'Sexo {sexo} registrado com sucesso ')

