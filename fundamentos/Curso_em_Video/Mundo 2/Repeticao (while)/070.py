gastos = 0
cont_caro = 0
produto_carovalor = 0
produto_caronome = ' '
while True:
	produto = input("Diga o nome do produto: ")
	valor = int(input("Diga o valor do produto: "))
	gastos =  gastos + valor
	if valor > produto_carovalor:
		produto_carovalor = valor
		produto_caronome = produto
		
	if valor > 1000:
		cont_caro += 1
	select = input('Deseja continuar [S/N]: ').upper()
	if select != 'S':
		break
	

print(f'O valor total dos gastos é {gastos}')
print(f'O total de produtos acima de R$ 1.000 é {cont_caro}')
print(f'O produto mais caro foi {produto_caronome} custando R$ {produto_carovalor}')