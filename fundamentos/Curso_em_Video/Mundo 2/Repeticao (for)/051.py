print('=' * 5, '10 Termos de Uma PA', '=' * 5)
soma = 0

num = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = num + (10 - 1) * razao

for x in range(num, decimo + razao, razao):
    print(x, end=' → ')
print('Acabou')
