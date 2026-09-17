# O programa sorteia um aluno para apagar a lousa, lendo os nomes e mostrando na tela o nome do escolhido.
import random
name1 = input('Digite o nome do primeiro aluno: ')
name2 = input('Digite o nome do segundo aluno: ')
name3 = input('Digite o nome do terceiro aluno: ')
name4 = input('Digite o nome do quarto aluno: ')
lista = [name1, name2, name3, name4]
sorteio = random.choice(lista)
print('O sorteado(a) foi {}'.format(sorteio))
