# Programa recebe duas notas do usuario, calcula e mostra sua media.
print('Calculo de media do aluno')
print('='*25)
nt1 = float(input('Digite a primeira nota: '))
nt2 = float(input('Digite a segunda nota '))
print('Os valores das notas são: {:.1f} e {:.1f}'.format(nt1,nt2))
print('A media do aluno é: {}'.format((nt1 + nt2) / 2))