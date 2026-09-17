print('Viagens ate 200km tem custo de 0.50R$ por km e viagens acima de 200km custam 0.45R$ por km')
viagem = int(input('Digite a distancia da viagem em km: '))
val1 = 0.50
val2 = 0.45

if viagem <= 200:
    print(f'Como a distancia é menor ou igual a de 200Km o valor da viagem de {viagem}km fica {val1 * viagem}R$')
else:
    print(f'Como a distancia é acima de 200Km o valor da viagem de {viagem}km fica {val2 * viagem}R$')