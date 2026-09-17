# O Programa lé o preço de um produto e aplica um desonto de 5%, mostrando seu novo preço.
val = float(input('Digite o valor do produto: '))
des = float(5 / 100) * val
new_val = float(val - des)
print(' '*20)

print('O valor deu: {:.2f}R$'.format(val))
print('O valor do desconto é: {:.2f}R$' .format(des))
print('O valor do produto com o desconto ficou: {:.2f}R$' .format(new_val))
