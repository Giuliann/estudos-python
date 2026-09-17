# O programa recebe o valor de uma casa e com base na pestação mensal ser maior que 30% do salario do comprador, aprova ou não um emprestimo.
val_casa = float(input('Qual o valor da casa: '))
sal = float(input('Qual o seu salario: '))
anos = int(input('Em quantos anos pretende Pagar o valor do emprestimo: '))


prestação = val_casa / (anos * 12)


if prestação > sal * 0.3:
    print('O Valor da prestação execede em 30' + '%', 'do seu salario')
    print('Situação do Emprestimo: NEGADO')
elif prestação < ((sal * 30) / 100) + sal:
    print('Situação do Emprestimo: Aprovado')
    print('O valo das prestações é {:.2f}R$' .format(prestação))