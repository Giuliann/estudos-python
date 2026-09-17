# O programa recebe um valor em graus celsius(ºC) e o converte em graus fahrenheit(ºF).
celsius = float(input('Informe a temperatura em (ºC): '))
fahrenheit = float(celsius * 1.8 + 32)
print('A temperatura de {}ºC corresponde a {}ºF' .format(celsius, fahrenheit))
