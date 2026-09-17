import random
cont = 0

while True:
    user_num = int(input('Digite um valor: '))
    user_select = input('Par ou Ímpar [P/I]: ').upper()
    comp_num = random.randint(0, 11)
    soma = (user_num + comp_num) % 2


    ### Usuario ganha ###
    if soma == 1 and user_select == 'I':
        print(f'Você jogou {user_num} e o computador {comp_num} total deu {user_num + comp_num}')
        print('A resposta é ÍMPAR, Parabéns você ganhou')
        cont += 1
    elif soma == 0 and user_select == 'P':
        print(f'Você jogou {user_num} e o computador {comp_num} total deu {user_num + comp_num}')
        print('A resposta é PAR, Parabéns você ganhou')
        cont += 1

    ### Usuario perde ###
    elif soma == 1 and user_select == 'P':
        print(f'Você jogou {user_num} e o computador {comp_num} total deu {user_num + comp_num}')        
        print('A resposta é ÍMPAR, que pena você errou')
        break
    elif soma == 0 and user_select == 'I':
        print(f'Você jogou {user_num} e o computador {comp_num} total deu {user_num + comp_num}')        
        print('A resposta é PAR, que pena você errou')
        break


print(f'Você venceu {cont} vezes')
