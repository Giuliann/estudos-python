print('Calcule seu IMC')
peso = float(input('Digite seu peso em (Kg): '))
altura = float(input('Digite sua altura em (m): '))
imc = float(peso / (altura * altura))

if imc < 18.5:
    print('Seu IMC é {:.1f} você está abaixo do peso ideal'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é {:.1f} você está no peso ideal'.format(imc))
elif imc >= 25 and imc <= 30:
    print('Seu IMC é {:.1f} você está sobrepeso'.format(imc))
elif imc >= 30 and imc <= 40:
    print('Seu IMC é {:.1f} você está Obeso'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.1f} você está com Obesidade Morbida'.format(imc))