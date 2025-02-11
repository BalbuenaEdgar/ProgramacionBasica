

print('Generar Número Aleatorios\n')

from random import randint

tamLista = 0
listaNumeros = []

while tamLista <= 0:
    tamLista = int(input('Cantidad de numeros aleatorios para generar: '))

while tamLista > 0:
    numeroRandom = randint(1,100)
    listaNumeros.append(numeroRandom)
    tamLista -= 1

for _ in range(len(listaNumeros)):
    print(f'{_ + 1}°: {listaNumeros[_]}')