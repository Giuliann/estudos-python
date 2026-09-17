print('Informe o valor de três  retas')
reta1 = float(input('Primeira reta: '))
reta2 = float(input('Segunda reta: '))
reta3 = float(input('Terceira reta: '))

if reta1 + reta2 > reta3 and reta3 + reta2 > reta1 and reta1 + reta3 > reta2:
    print('Forma um tiangulo')
    if reta1 == reta2 == reta3:
        print('Triangulo Equilatero')
    elif reta1 == reta2 or reta2 == reta3 or reta3 == reta1:
        print('Triangulo Isósceles')
    elif reta1 != reta2 != reta3 != reta1:
        print('Triangulo Escaleno')
else:
    print('Não é um triangulo')