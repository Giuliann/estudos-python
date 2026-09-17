# O programa que lé dois valores e mostre um menu na tela, o programa realizara a operação solicitada em cada caso.
num = int(input('Digite o primeiro valor: ')) 
num2 = int(input('Digite o segundo valor: '))

print('[1] Somar')
print('[2] Subtrair')
print('[3] Multiplicar')
print('[4] Dividir')
print('[5] Fechar programa')
select = int(input('Selecione uma opção: '))

while select not in (1,2,3,4,5):
    print('\nSelecione uma opção valida:')
    print('[1] Somar')
    print('[2] Subtrair')
    print('[3] Multiplicar')
    print('[4] Dividir')
    print('[5] Fechar programa')
    select = int(input('Selecione uma opção: '))

if select == 1:
    soma = num + num2
    print(f'A soma dos valores {num} e {num2} resulta em: {soma}')
elif select == 2:
    subtracao = num - num2
    print(f'A subtração dos valores {num} e {num2} resulta em: {subtracao}')
elif select == 3:
    multiplicacao = num * num2
    print(f'A multiplicação dos valores {num} e {num2} resulta em: {multiplicacao}')
elif select == 4:
    dividir = num / num2
    print(f'A divisão dos valores {num} e {num2} resulta em: {dividir}')
elif select == 5:
    input('Pressione ENTER para fechar o programa...')
    exit('Fim do Programa')

