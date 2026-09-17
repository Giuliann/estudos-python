# O Programa le o nome dos quatro alunos e mostre a ordem sorteada.

import random

nome1 = input('Digite o nome do primeiro aluno: ')
nome2 = input('Digite o nome do segundo aluno: ')
nome3 = input('Digite o nome do terceiro aluno: ')
nome4 = input('Digite o nome do quarto aluno: ')

lista = [nome1, nome2, nome3, nome4]

random.shuffle(lista)
print(f'\n\na ordem será {lista}')
