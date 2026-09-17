# O programa lé o nome de uma cidade e diz se ela começa ou não com o nome “SANTO”.
cidade = str(input('Digite o nome de uma cidade: ')).strip
uper = str.upper(cidade)
result = str.upper(cidade).startswith('SANTOS')


if result == True:
    print(f'A cidade {cidade} inicia com Santos ')

else:
    print(f'A cidade {cidade} não inicia com Santos ')

