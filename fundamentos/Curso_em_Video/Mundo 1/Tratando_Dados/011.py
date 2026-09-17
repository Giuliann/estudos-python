# O programa le o valor de altura e largura de uma parede em metros(m), calcula sua área e quantidade de tinta necessaria para pintala.
print('   '*20)
alt = int(input('Digite a altura da parede em metros(m): '))
lar = int(input('Digite a largura da parede em metros(m): '))
print('   '*20)
area = lar * alt
tinta = int(area / 20)
print('As especificaçôes da sua parede são: Altura {}m e Largura {}m\n' .format(alt,lar))
print('O valor da area da sua parede é: {}m²\n' .format(area))
print('Você precissara de {}L litros de tinta\n' .format(tinta))