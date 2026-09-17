# Programa recebe o valor de um salário de funcionário e mosta seu novo salário com um aumento de 15%.
print('Qual o salario do funcionário: ')
sal = float(input())
aumento = float((15 / 100) * sal)
new_sal = float(aumento + sal)
print('O funcionário que recebia {:.2f}R$. Agora com o aumento recebe {:.2f}R$' .format(sal, new_sal))
print('Teve aumento de {:.2f}R$'.format(aumento))
