# O programa recebe um ano e analisa se o ano é bissexto
from datetime import date

anoI = input('Digite um ano ou 0 para analisar o ano atual:')    
ano = int(anoI)
cent = anoI.endswith('00')


if ano == 0:
    ano = date.today().year

    if cent == True:
        b = ano % 400

        if b == 0:
            print(f'O ano {ano} é um ano centenario bissexto')
        else:
            print(f'O ano {ano} é um ano centenario não bissexto')
    else:
        a = ano % 4

        if a == 0:
            print(f'O ano {ano} é um ano que não é centenario mas é bissexto')
        else:
            print(f'O ano {ano} é um ano que não é centenario e também não é bissexto')