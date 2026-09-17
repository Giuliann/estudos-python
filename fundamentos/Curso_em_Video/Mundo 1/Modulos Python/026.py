# O programa que lé uma frase pelo teclado e mostra quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input('Digite uma frase: ').upper().strip()
a = frase.count('A')
local = frase.find('A')
local1 = frase.rfind('A')

print(f'A letra A aparece {a} vezes nessa frase')
print(f'A posição do primeiro A é: {local + 1}')
print(f'A ultima posição do A é: {local1 + 1}')
