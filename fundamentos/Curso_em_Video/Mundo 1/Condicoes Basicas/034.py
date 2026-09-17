# Programa exibe um aumento de valor de um salario de um funcionario promovido de acordo com o salário.
sal = float(input('Digite seu Salário: '))

if sal > 1250:
    new_sal = (sal * 10 / 100) + sal
    print('Parabéns pela promoção seu novo salário é {:.2f} R$' .format(new_sal))
else:
    new_sal = (sal * 15 / 100) + sal
    print('Parabéns pela promoção seu novo salário é {:.2f} R$' .format(new_sal))