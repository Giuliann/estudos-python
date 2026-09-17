# O programa lé um ângulo qualquer digitado pelo teclado e exibe o valor do Seno(sen), Cosseno(cos) e Tangente(tan) desse angulo.
import math
ang = float(input('Digite o ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo {} tem seno de {:.2f}'.format(ang,sen))
print('O ângulo {} tem cosseno de {:.2f}'.format(ang,cos))
print('O ângulo {} tem tangente de {:.2f}'.format(ang,tan))