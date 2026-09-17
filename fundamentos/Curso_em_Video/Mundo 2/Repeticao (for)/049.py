print('=' * 5, 'Escolha Uma Opção' , '=' * 5)
for x in range(1, 11):
    print(f'({x}) Tabuada do {x}')

select = int(input())
multi = 0
for x in range(0,11):
    if select == x:

        for x in range(0, 11):
            resp = select * x
            print(f'{select} x {x} = {resp}')