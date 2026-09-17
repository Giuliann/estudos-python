# O programa que lé duas notas de um aluno e calcula sua média, mostrando uma mensagem no final, de acordo com a média atingida.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('Aluno Reprovado')
elif media > 5.0 and media < 7.0:
    print('Aluno de recuperação')
elif media >= 7:
    print('Aluno foi Aprovado')