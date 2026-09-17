# O programa lé o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade.
from datetime import datetime
ano_atual = datetime.today().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - nascimento

if idade <= 9:
    print(f'Sua idade é {idade} então você é um atleta Mirim')
elif idade > 9 and idade <= 14:
    print(f'Sua idade é {idade} então você é um atleta Infantil')
elif idade > 14 and idade <= 19:
    print(f'Sua idade é {idade} então você é um atleta Junior')
elif idade > 19 and idade <= 25:
    print(f'Sua idade é {idade} então você é um atleta Senio')
elif idade > 25:
    print(f'Sua idade é {idade} então você é um atleta Master')