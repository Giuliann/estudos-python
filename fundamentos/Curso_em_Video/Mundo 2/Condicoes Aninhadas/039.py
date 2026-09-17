# O programa le o ano de nascimento de um jovem e informa, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar.
from datetime import date

ano_atual = date.today().year
seu_ano = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - seu_ano

if idade < 18:
    print('Você nsaceu em {} e tem {}' .format(seu_ano, idade))
    print('Você precisara se alistar em {} anos.' .format(18 - idade))
    print('Seu alistamento será em {}' .format(seu_ano + 18))
elif idade > 18:
    print('Você nsaceu em {} e tem {}' .format(seu_ano, idade))
    print('Você passou {} anos do tempo de alistamento.' .format(idade - 18))
    print('Seu alistamento foi {}' .format(seu_ano + 18))
elif idade == 18:
    print('Você nasceu em {}' .format(seu_ano))
    print('Você tem {} anos, este é o momento certo para se alistar.' .format(idade))