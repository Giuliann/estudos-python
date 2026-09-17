num = int(input('Digite um valor: '))
media = num
maior = num
menor = num
cont = 1

select = input('Deseja continuar [S] sim e [N] não: ').upper()
while select == 'S':
    cont += 1
    num = int(input('Digite um valor: '))
    select = input('Deseja continuar [S] sim e [N] não: ').upper()
    media += num
    if num > maior:
        maior = num
    elif num < menor and num > 0:
        menor = num

print(f'O maior número digitado foi {maior} e o menor número foi {menor}')
print(f'A media dos {cont} números digitados é igual a {media / cont}')