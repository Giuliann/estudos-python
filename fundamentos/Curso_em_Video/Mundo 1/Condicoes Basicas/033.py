# Compara três valores e informar qual deles é o maior valor e qual o menor valor.
print('Digite três números')
x = int(input('Primeiro número: '))
y = int(input('Segundo número: '))
z = int(input('Terceiro número: '))

if x<y and x<z:
    menor = x
elif y<x and y<z:
    menor = y
elif z<x and z<y:
    menor = z

if x>y and x>z:
    maior = x
elif y>x and y>z:
    maior = y
elif z>x and z>y:
    maior = z

print(f'Maior valor foi: {maior}')
print(f'Menor valor foi: {menor}')