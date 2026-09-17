compras = float(input('Total das compras: R$'))
print('=' * 30)
print('Formas de Pagamento')
print('(1) A vista pix/dinheiro')
print('(2) A vista Cartão')
print('(3) 2x no Cartão')
print('(4) 3x ou mais no Cartão com juros')
select = int(input('Qual opção: '))

if select == 1:
     desconto = (compras / 100) * 10
     print('Parabéns você obteve um desconto na sua compra de 10% igual a {:.2f}R$, o valor da compra ficou {:.2f}R$'.format(desconto, compras - desconto))
elif select == 2:
     desconto = (compras / 100) * 5
     print('Parabéns você obteve um desconto na sua compra de 10% igual a {:.2f}R$, o valor da compra ficou {:.2f}R$'.format(desconto, compras - desconto))
elif select == 3:
     parcela = compras / 2
     print('O preço final das suas compras ficou em {:.2f}R$ com as parcelas de duas vezes com valor de {:.2f}R$ no cartão de credito.' .format(compras, parcela))
elif select == 4:
     parcelas = float(input('Quantas parcelas: '))
     jurus = (compras / 100) * 20 
     parcela = (compras + jurus) / parcelas 
     print('Você optou por {:.0f} parcelas no cartõa com juros, o valor das compras ficaram {:.2f}R$, com as parcelas no valor de {:.2f}R$ no cartão de credito.'.format(parcelas, compras + jurus, parcela))
else:
     print('Selecione uma opção valida...')