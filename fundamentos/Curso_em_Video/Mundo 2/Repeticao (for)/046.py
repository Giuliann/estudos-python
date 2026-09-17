from time import sleep
print('Contagem regresiva')

for x in range(10, -1, -1):
    print(x)
    sleep(1)
print('*' * 5,'FOGOS', '*' * 5)
